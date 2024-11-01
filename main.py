from src.case_study_line_drawing_using_raspberrypi import logger
import cv2
from src.case_study_line_drawing_using_raspberrypi.pipeline.stage_01_Background_remover_with_watermark import BackgroundRemoverAndWatermarkPipeline

STAGE_NAME = 'Background Remover with watermark Stage'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = BackgroundRemoverAndWatermarkPipeline()
    image = obj.main()
    # cv2.imwrite("artifacts/Image_with_watermark_at_top.jpg",image)
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e