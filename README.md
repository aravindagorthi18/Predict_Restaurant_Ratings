# Predict_Restaurant_Ratings
Here's a simple explanation of what we did in these 5 steps of Task 1:

### Step 1: Data Preprocessing
We prepared our restaurant data so machine learning algorithms could use it properly. This included:
- Handling missing values by filling them in with reasonable estimates
- Converting text categories into numbers (one-hot encoding)
- Splitting our data into training data (to learn from) and testing data (to evaluate our model)
- Standardizing numerical values so they're all on a similar scale

### Step 2: Model Training
We built several different machine learning models to predict restaurant ratings:
- Linear Regression: A simple model that finds linear relationships between features and ratings
- Decision Tree: A model that makes decisions based on feature thresholds
- Random Forest: A powerful model that combines many decision trees

Each model learned patterns from our training data to predict restaurant ratings based on other factors.

### Step 3: Model Evaluation
We measured how well each model performed by:
- Calculating how far off predictions were from actual ratings (Mean Squared Error)
- Determining what percentage of the rating variation our model explains (R-squared)
- Creating visualizations to see actual vs. predicted ratings
- Examining the errors (residuals) to check for patterns

### Step 4: Feature Importance Analysis
We identified which restaurant characteristics most strongly influence ratings:
- For Random Forest, we extracted feature importance values
- For Linear Regression, we analyzed coefficients
- We visualized the most important features to understand what drives restaurant ratings

### Step 5: Interpretation
We made sense of our results by:
- Determining which model performed best
- Explaining how much of the variation in restaurant ratings we can predict
- Identifying the most important factors affecting restaurant ratings
- Providing recommendations based on our findings

In essence, we built a system that can predict a restaurant's rating based on its characteristics, and we discovered which factors matter most for restaurant success.

TASK 2:Predicting Restaurant Ratings
Here's a brief summary of what we did to build a machine learning model for predicting restaurant ratings:

1. **Data Exploration**: We started by loading the dataset and examining its structure, including column names and basic statistics, to understand what we're working with.

2. **Feature Selection**: We identified which columns to use as features, separating them into categorical variables (like cuisine type or location) and numerical variables (like price range or number of votes).

3. **Data Preprocessing**: We created pipelines to handle missing values and transform the data appropriately - scaling numerical features and one-hot encoding categorical variables.

4. **Model Training**: We implemented two different regression algorithms:
   - Linear Regression as a baseline model
   - Random Forest Regression as a more complex model

5. **Model Evaluation**: We assessed model performance using standard regression metrics:
   - Mean Squared Error (MSE)
   - R-squared (coefficient of determination)
   - Root Mean Squared Error (RMSE)

6. **Feature Importance Analysis**: For the Random Forest model, we identified and visualized which features had the strongest influence on restaurant ratings.

7. **Visualization**: We created several visualizations to interpret the results:
   - Feature importance bar charts
   - Actual vs. predicted rating scatter plots
   - Residual analysis plots

8. **Debugging**: We addressed a key error that occurred because the column names in the code didn't match those in the actual dataset, demonstrating the importance of data exploration before modeling.

This approach provides a complete machine learning pipeline for predicting restaurant ratings and understanding which factors most influence those ratings.
