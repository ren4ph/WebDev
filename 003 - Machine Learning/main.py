import pandas as pd
import joblib, sys

with pd.load("music_reccomendations.joblib") as f:
  print(f)

  if f.open:
    f.close()
    sys.exit()

print("Didn't work!")
