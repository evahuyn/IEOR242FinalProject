# IEOR 242 Final Project: RateMyProfessors: Better Learning & Teaching

Group 8: Yanbo Wang, Yinuo Hu, Jiaming Xiong, Shichen Wu and Xinlin Huang

This github repo includes data and code for reproducing the result of our final report. 

## Data Preparation

Under data_preparation folder, we have several files to collect data from web scraping and pre-process all the dataset into train and test sets.

- Package used: requests, lxml, xpath

- `RMP_web_crawler.py` : generate 6712 csv about professors, 141729 student comments
(too large for original files, so just see uncleaned_data.csv for demonstration)

- Note: change user-agent based on your personal browser & pageNum parameter for page scraping

- After dropping NAs, we acquired `Uncleaned_data.csv`

- Run `Data_Cleansing.ipynb` will generate `RMP_cleaned.csv`

- Run `train_test_split.ipynb` will generate train and test csv. See data folder for more raw and clean datasets.

## Models

### Logistic Regression

See: `models/Logistic_Regression.ipynb`
Run the codes in order.

### Linear Discriminant Analysis

See `models/LDA.ipynb`
Run the codes in order.

### Classification and Regression Trees

See `models/CART.ipynb` 
Run the codes in order.

### Random Forest

See `models/RandomForest.ipynb`
Run the codes in order.

### Sentiment Analysis - Comments

See `models/NLP.ipynb`
Run the code in order.

### Topic Model - LDA

```commandline
cd topic-model
```

To reproduce topic model results, we need to firstly install all dependencies. Run the following command in the command line:

```commandline
npm install
```

Train the model
```commandline
python TopicModel.py
```

To view LDA visualization, run the following command and open up localhost:3000 on browser.

```commandline
npm start
```
