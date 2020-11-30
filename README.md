# BizViz: Powering Small Businesses to Make the Best Financial Decisions :chart_with_upwards_trend: :dollar: #

*HackGT 7 Hackathon Submission (Awarded Top 8 out of 175+ projects at HackGT 7)* 🏆
### BizViz is a financial business visualization tool that gives small business owners insight into different ways to keep their business operating during difficult times like the COVID-19 global pandemic. Instead of having businesses collapse due to owners continuing to spend more money to keep themselves growing, our application takes that same monetary value and instead shows what would be a reasonable return if that money was invested into different types of stock market portfolios. All this data is then presented to the user to allow them to better gauge whether it would be worthwile to divert funds into investments while the pandemic is active to potentially make a profit to keep the business operating for longer.

## Some of the technologies we used include:
![React](https://img.icons8.com/ios/150/000000/react-native.png)
![Flask](https://www.olirowan.xyz/static/images/icons/flask-plain.svg)
![IBM Watson](https://github.com/varunlakshmanan/hackgt7/blob/main/watson3.png)
![SciKitLearn](https://github.com/varunlakshmanan/hackgt7/blob/main/sklearn.png)

## How it works ##

When the user first visits the site, they will be prompted to enter some data about the business. The user first selects a number of months to look ahead to make a prediction. After that, the user inputs what they anticipate will be the future costs will be for the next number of months they selected. This input data should be estimates for the future costs they spend for wages, advertising, fixed costs, and other miscellaneous costs, as well as whether the business is run online or in person. Then, the user will submit an csv file that has the total companies monthly costs (fixed + variable costs, advertising, wages) and their monthly revenue for the past 10 years. This data is then parsed and processed for training of our machine learning algorithm that is chosen from an ensemble of models that is optimized for our data. This model then outputs predicted revenue based on the business' performance.

Taking into account the projected revenue, we created another ML model to forecast the projected values of simulated portfolios if the specified amount was invested in the stock market instead. We then used the IBM Watson cloud to upload and deploy our ML model so it can be used for other applications in the future. This gives us great flexibility in the predictions we wish to perform.

The custom stock portfolios have 3 categories: Low Risk, Medium Risk, and High Risk. The low risk is composed of non-volatile options such as index funds and bonds, while the high risk option is comprised of stocks with high volume, high market cap, and other indicators of volatile stocks.

The predicted revenue, and the predicted growth of the 3 suggested stock portfolios are plotted on a graph to provide the business owner with a simple and effective way to decide whether it could potentially be beneficial if they invested in the portfolio instead of putting that into the business. 


## Team: ##
* *Yash Patel ([@yashp121](https://github.com/yashp121))*
* *Nishant Ravi ([@NRavi01](https://github.com/NRavi01))*
* *Varun Lakshmanan ([@varunlakshmanan](https://github.com/varunlakshmanan))*
* *Pranav Pusarla([@PranavPusarla](https://github.com/PranavPusarla))*
