from PIL import ImageGrab
import numpy as np
import cv2



# graal era widthxheight = 770x610

def get_screen(topx=20, topy=221, bottx=780, botty=815):
  screen = np.array(ImageGrab.grab(bbox=(topx, topy, bottx, botty)))
  screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

  return screen


if __name__ == '__main__':
  while True:
    screen = get_screen()

    cv2.imshow("window", screen)
    if cv2.waitKey(25) & 0xFF == ord("q"):
      cv2.destroyAllWindows()
      break
