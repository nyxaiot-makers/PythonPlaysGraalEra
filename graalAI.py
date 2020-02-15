import numpy as np
import time
from datetime import datetime
import sys, os
from utils import screen, directkeys, getkeys


class GraalAI(object):

  def __init__(self, name=None, model_filepath=None, savepath=None):
    self.name = name
    self.model_filepath = model_filepath
    self.savepath = savepath

    # IJKLASD
    self.key2int = {
      "I": 0,
      "J": 1,
      "K": 2,
      "L": 3,
      "A": 4,
      "S": 5,
      "D": 6
    }

    self.int2key = {
      0: directkeys.I,
      1: directkeys.J,
      2: directkeys.K,
      3: directkeys.L,
      4: directkeys.A,
      5: directkeys.S,
      6: directkeys.D
    }

    print(f"[{self.name}] has been initialized successfully!")

  def countdown(self, seconds=4):
    for i in range(seconds):
      print(seconds-i)
      time.sleep(1)


  def record(self, exit_key="Y", batch_size=1000,  action_memory=8):
    self.countdown()
    print("Record started!\n")
    pass_actions = list()
    pressed_key = list()
    frames = list()

    pressing = list()
    actions = list()
    last_time = time.time()
    while exit_key not in pressing:
      pressing = getkeys.key_check()
      frame = screen.get_screen()

      if len(pressed_key) % 100 == 0:
        print(f"Frames recorded: {len(pressed_key)}")

      if len(pressed_key) >= batch_size:
        print(f"Batch took: {time.time()-last_time}")
        last_time = time.time()
        # create timestamp base on date and time
        timestamp = str(datetime.now()).split(".")[0].replace(":", "-")
        with open(f"{self.savepath}/RECORDING_{timestamp}.npy", "wb") as save_file:
          np.save(file=save_file, arr=np.array([frames, pass_actions, pressed_key]))
        pass_actions = list()
        pressed_key = list()
        frames = list()
        print("Saved!\n\nResume recording...")

      if exit_key not in pressing:
        if pressing:
          for p in pressing:
            if p in list("ASD"):
              actions.append(self.key2int[p])

        if len(actions) > action_memory:
          actions = actions[-action_memory:]
        pressed_key.append([self.key2int[p] for p in pressing if p != "\x08"])
        frames.append(frame)
        pass_actions.append(actions)


  def load_data(self):
    # data = list()
    for i, f in enumerate(os.listdir(self.savepath)):
      print(f"Loading file: {i+1}")
      with open(f"{self.savepath}/{f}", "rb") as read_file:
        data = np.load(read_file, allow_pickle=True)

      break

    # [[frames], [history], [curr_key]]

    print(data[0][21])
    print(data[1][21])
    print(data[2][21])




if __name__ == "__main__":
  os.chdir(os.path.dirname(os.path.realpath(__file__)))
  sys.path.insert(0, os.getcwd())
  SAVEPATH = "./recordings"
  MODEL_FILEPATH = "./models"
  NAME = "Dig Shell Bot"

  graal_bot = GraalAI(name=NAME, model_filepath=MODEL_FILEPATH, savepath=SAVEPATH)
  # graal_bot.record()
  graal_bot.load_data()

