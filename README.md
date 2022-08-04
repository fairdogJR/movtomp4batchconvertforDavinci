# movtomp4batchconvertforDavinci is a simple script for python that calls handbrakecli process to batch convert mov to mp4. since Davinci resolve does not diretcly take mov files . 
you need to install handbrake cli first and either add to your path or pop it in your working directory . 

https://handbrake.fr/rotation.php?file=HandBrakeCLI-1.5.1-win-x86_64.zip

https://handbrake.fr/rotation.php?file=HandBrakeCLI-1.5.1-win-x86_64.zip![image](https://user-images.githubusercontent.com/11721205/182749275-f2249e0f-6ead-411e-99e8-78ddb7e1c905.png)
for example on the command line you woul have to do this:
    HandBrakeCLI -e x264 -q 20.0 --input IMG_3331.MOV --output IMG_3331.mp4![image](https://user-images.githubusercontent.com/11721205/182749317-1a4ac1b4-2130-4df6-871c-20b50804e57d.png)

This is a work in process so you will have to put your custom path in the code for now
