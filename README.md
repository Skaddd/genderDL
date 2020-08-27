# genderDL


This repo contains a GUI using Deep learning.
Note that this project was created on Windows 10, you should probably check paths variable if you want to run it on different OS




## The GUI

This application requires a webcam
The app has two main functionality, applying gender and age prediction combined with face recognition on a image taken from the webcam. Then the automatically result is displayed.
The second functionality is about fast style transfer. You will be able to apply style transfer to your image, given different style.

To launch the application you just need to run the first Window
```bash
python Window1.py
```
It's important to not that my pre-trained model are not in this repo

## Training

you can train your own models, however you need to download the adience database and create a repo named `data/` then directly put the folds inside. Finally you add the 
`aligned/` folder to it

Now you can try your model
It's important to note that the model for age and gender are sperarted( the results were better this way)
so you might want to go in `train.py` to change which model you want.

```python
COUNT = 0 # for gender model
COUNT = 1 #for age model
```
the models will be automatically stored in `models/`

Launch the training

```bash
python train.py
```

## Results of the AgeGenderDL


We created two separate model:
the gender model reached 96% of accuracy on validation set
the age model was close de 58% of accuracy on validation set
