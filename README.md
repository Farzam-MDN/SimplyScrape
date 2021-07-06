# SimplyScrape


<!---
![SimplyScrape Logo](https://i.imgur.com/X12ZeEE.png)
-->



SimplyScrape is a tool that makes web scraping esier for you. SimplyScrape generates web-scraping code for you automatically. All you need to do is to fill in the input fields!

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need the following in order to run the application as it is intended on your machine:

```
Python 3 or above
Pip package installer for python

```

### Installing the application

First clone this repository or download it manually to a working directory on your computer.
Thereafter, open terminal/cmd inside the SimplyScrape directory on your computer.
Now Run the following command in your terminal/cmd:

```
pip install -r requirements.txt
```
After all the requirements are installed, you need to download a Chrome WebDriver. Go to https://chromedriver.chromium.org/downloads or simply click [here](https://chromedriver.chromium.org/downloads).
Now download the latest version of Chrome WebDriver. Extract the downloaded zip file downloaded. Now copy the extracted file (named 'chromedriver.exe') and paste it into SimplyScrape directory. Lastly update your chrome browser to the latest version available (this step is highly suggested for better performance of the tool).
The SimplyScrape directory on your machine should look something like the image below:

![SimplyScrape Directory](https://i.imgur.com/I5Rzqa5.png)



### Running the application 

if you have gone throgh the steps of "Installing the application" chapter, you are ready to use the SimplyScrape tool. Open cmd/terminal and run the following command:

```
py SimplyScrape.py
```

Now the tool should prompt you to name your web scraping session. Name it anything you like.
Afterwards the tool prompts you to provide a url to a page you want to webscrape. Provide the full url of the webpage you want to scrape to the application. Now the application will open a browser window as well as an html code.
The chrome browser window will connect to the webpage you wanted to scrape. Inside the chrome browser window you can use the chrome developer tools to inspect the webpage. The html code that is opened for you is the html code of the webpage you provided to the tool. You can look through the html code for better understanding the structure of the website. The html code for the webpage is stored in the 'SimplyScrape' directory. 
Now go back to the terminal that previously prompted you for inputs (the terminal/cmd that is running SimplyScrape).
You should be prompted to provide class name of a span element. You can choose to leave it empty or you can provide class name of a span element in the webpage you chose. After filling the input and submitting you will have more inputs asking for class names of specific elements. You can leave them empty or provide class names for those elements in case you want to extract information from those classes. 
After you have submitted information for all the input fields the application will open a text file containing code that can be used for web scraping the page you provided the tool. 


## Contributing

Feel free to fork and expand this project! Send a pull request if you would like to add your code to the project.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/farzammadani/JustShareKeys/releases). 

## Authors

* **Farzam Madani** - *Creation of the core application* - [farzammadani](https://github.com/farzammadani)

See also the list of [contributors](https://github.com/farzammadani/JustShareKeys/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/farzammadani/JustShareKeys/blob/master/LICENSE) file for details

## Acknowledgments

* Big thanks to anyone whose library is used for this project 


