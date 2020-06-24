# Bank-Reviews-Complaints-Analysis

## Table of Content
  * [Directory Tree](#directory-tree)
  * [BUSINESS PROBLEM](#business-problem)
  * [OBJECTIVE](#objective)
  * [DATASET](#dataset)
  * [How to Use](#how-to-use)
  * [LICENSE](#license)

### Directory Tree

```
├── results
│   ├── 2020-06-21 16_52_49-Window.png
│   ├── 2020-06-21 16_53_18-Window.png
│   ├── 2020-06-21 16_53_57-Window.png
│   ├── 2020-06-21 16_58_01-Window.png
├── static
│   ├── styles.css
├── templates
│   ├── home.html
│   ├── result.html
├── app.py
├── Dockerfile
├── nlp_model.pkl
├── Bank Reviews-Complaints Analysis.ipynb
├── transform.pkl
├── tfidf_transform.pkl
├── requirements.txt
├── LICENSE
├── Procfile
├── README.md
```

### BUSINESS PROBLEM :

Central banks collecting information about customer satisfaction with the services provided by different bank. Also collects the complaints.

Bank users give ratings and write reviews about services on central bank websites. These reviews and ratings help to banks evaluate services provided and take necessary to action improve customer service. While ratings are useful to convey the overall experience, they do not convey the context which led a reviewer to that experience. 

If we look at only the ratings, it is difficult to guess why the user rated the service as 4 stars. However, after reading the review, it is not difficult to identify that the review talks about good "service" and "expectation".

### OBJECTIVE :

The objective is to analyze customer reviews and predict customer satisfaction with the reviews.

1) Data preprocessing.
2) Key possitive words/negative words (most frequent words).
3) Classification of reviews into positive, negative and neutral.
4) Identify key themes of problems (using clustering, topic modeling).
5) Predicting star ratings using reviews.
6) Perform intent analysis.

### DATASET :

The data is detailed dump of customer reviews/ complaints (~500) of different services at different banks.

1) Date : Day the review was posted.
2) Stars : 1-5 ratings for the business.
3) Reviews : Review text.
4) BankName : Name of the bank.

### How to Use

Just follow 3 simple steps :

1. Go to project website link https://warm-ridge-56434.herokuapp.com/ .<br>

2. Write a Review for Bank as shown below :<br><br>

![](https://github.com/vicky60629/Bank-Reviews-Complaints-Analysis/blob/master/results/2020-06-21%2016_52_49-Window.png)<br>

3. Then Click on Predict and you get the Ratings of your review from 1 to 5 .<br><br>

![](https://github.com/vicky60629/Bank-Reviews-Complaints-Analysis/blob/master/results/2020-06-21%2016_53_18-Window.png)<br>

**If you face any problem :** email me at *vg60629@gmail.com*

### License

[MIT License](https://github.com/vicky60629/Bank-Reviews-Complaints-Analysis/blob/master/LICENSE)

Copyright (c) 2020 Vicky Gupta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
