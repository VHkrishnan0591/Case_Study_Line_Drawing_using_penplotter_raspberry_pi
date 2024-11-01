from src.case_study_line_drawing_using_raspberrypi.components.back_ground_remover import Backgroundremover
from src.case_study_line_drawing_using_raspberrypi import logger
import cv2 

STAGE_NAME = 'Background Remover with watermark Stage'

class BackgroundRemoverAndWatermarkPipeline:
    
    def __init__(self):
        pass

    def main(self):
        # config = ConfigurationManager()
        bg_remover = Backgroundremover()
        image = cv2.imread("research/cat_image.jpg")
        logger.info(f">>>>>> stage background remover started <<<<<<")
        image = bg_remover.background_remover(image)
        # cv2.imwrite("artifacts/Image_with_white_bg.jpg",image)
        logger.info(f">>>>>> stage background remover ended <<<<<<")
        logger.info(f">>>>>> stage watermarker adder started <<<<<<")
        image = bg_remover.watermark_at_top_right(image)
        logger.info(f">>>>>> stage watermark adder ended <<<<<<")
        return image
        # cv2.imwrite("artifacts/Image_with_watermark_at_top.jpg",image)
        
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = BackgroundRemoverAndWatermarkPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


