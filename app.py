from flask import Flask, render_template, request, url_for, send_from_directory, redirect
from src.case_study_line_drawing_using_raspberrypi.constants import *
from src.case_study_line_drawing_using_raspberrypi.utils.commons import read_yaml
from src.case_study_line_drawing_using_raspberrypi.pipeline.stage_01_Background_remover_with_watermark import BackgroundRemoverAndWatermarkPipeline
from src.case_study_line_drawing_using_raspberrypi import logger
import cv2
import io
import datetime
import os

app = Flask(__name__)

config_filepath = CONFIG_FILE_PATH
params_filepath = PARAMS_FILE_PATH

config = read_yaml(config_filepath)
params = read_yaml(params_filepath)

os.makedirs(config['upload_image_folder']['path'], exist_ok=True)
os.makedirs(config['processed_image_folder']['path'], exist_ok=True)

STAGE_NAME = 'Background Remover with watermark Stage'

@app.route('/')
def upload_page():
    return render_template('index.html', processed_image = False)

@app.route('/upload', methods=['POST'])
def upload_image():
        if 'image' not in request.files:
            return redirect('index.html')

        file = request.files['image']
        if file.filename == '':
            return redirect('index.html')

        if file:
            filename = file.filename
            file_path_of_uploaded_file = os.path.join(config['upload_image_folder']['path'], filename)
            file.save(file_path_of_uploaded_file)
            print(file_path_of_uploaded_file)
        try:
            logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
            obj = BackgroundRemoverAndWatermarkPipeline()
            image = obj.main()
            filename = params['processed_image_file_base_name']+".jpg"
            file_path_of_processed_image = os.path.join(config['processed_image_folder']['path'], filename)
            print(file_path_of_processed_image)
            cv2.imwrite(file_path_of_processed_image,image)
            logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e
        return render_template('index.html', processed_image=True, file_path_of_processed_image = file_path_of_processed_image, file_path_of_uploaded_image = file_path_of_uploaded_file)

# @app.route('/static/<path:path>')
# def send_static_file(path):
#     return send_from_directory('static', path)
    
if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
