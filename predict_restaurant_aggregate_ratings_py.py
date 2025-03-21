# -*- coding: utf-8 -*-
"""predict restaurant aggregate ratings.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IEC0Qap-wIJisZlq735qQVYw6Ztt7LR9
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Dataset_Cognify.csv')

# Explore the dataset structure
print("Dataset shape:", df.shape)
print("\nColumn names in the dataset:")
print(df.columns.tolist())
print("\nData preview:")
print(df.head())
print("\nData types:")
print(df.dtypes)
print("\nMissing values:")
print(df.isnull().sum())
print("\nSummary statistics:")
print(df.describe())

# After running this code, identify your rating column
# For example: rating_column = 'rating'

# Set your rating column based on exploration in Step 1
rating_column = 'Aggregate rating'  # Replace with actual column name

# Visualize distribution of ratings
plt.figure(figsize=(10, 6))
sns.histplot(df[rating_column], kde=True)
plt.title(f'Distribution of {rating_column}')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

# Identify categorical and numerical columns
# Replace these with your actual columns
categorical_cols = []  # e.g., ['cuisine_type', 'city', 'has_delivery']
numerical_cols = []    # e.g., ['price', 'num_reviews', 'avg_cost']

# For automatic detection (alternative approach):
categorical_cols = []
numerical_cols = []
for col in df.columns:
    if col == rating_column:
        continue
    if pd.api.types.is_numeric_dtype(df[col]):
        numerical_cols.append(col)
    else:
        categorical_cols.append(col)

print("Categorical columns:", categorical_cols)
print("Numerical columns:", numerical_cols)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# Separate features and target
X = df.drop(rating_column, axis=1)
y = df[rating_column]

# Create preprocessor for numerical data
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Create preprocessor for categorical data
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combine preprocessors
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Create Linear Regression Pipeline
lr_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# Train the model
lr_pipeline.fit(X_train, y_train)

# Make predictions
y_pred_lr = lr_pipeline.predict(X_test)

# Evaluate performance
mse_lr = mean_squared_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)
rmse_lr = np.sqrt(mse_lr)

print("Linear Regression Results:")
print(f"Mean Squared Error: {mse_lr:.4f}")
print(f"R-squared: {r2_lr:.4f}")
print(f"Root Mean Squared Error: {rmse_lr:.4f}")

from sklearn.ensemble import RandomForestRegressor

# Create Random Forest Pipeline
rf_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train the model
rf_pipeline.fit(X_train, y_train)

# Make predictions
y_pred_rf = rf_pipeline.predict(X_test)

# Evaluate performance
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)
rmse_rf = np.sqrt(mse_rf)

print("Random Forest Results:")
print(f"Mean Squared Error: {mse_rf:.4f}")
print(f"R-squared: {r2_rf:.4f}")
print(f"Root Mean Squared Error: {rmse_rf:.4f}")

# Analyze feature importance (for Random Forest)
if hasattr(rf_pipeline.named_steps['regressor'], 'feature_importances_'):
    try:
        # Get preprocessor and feature names
        preprocessor = rf_pipeline.named_steps['preprocessor']

        # Try for newer scikit-learn versions
        ohe = preprocessor.named_transformers_['cat'].named_steps['onehot']
        cat_feature_names = list(ohe.get_feature_names_out(categorical_cols))
        feature_names = numerical_cols + cat_feature_names
    except:
        # Fallback for older versions
        feature_names = []
        for i, col in enumerate(numerical_cols + categorical_cols):
            feature_names.append(f"Feature_{i}_{col}")

    # Get and sort feature importances
    importances = rf_pipeline.named_steps['regressor'].feature_importances_
    indices = np.argsort(importances)[::-1]

    # Plot feature importances (top 20)
    plt.figure(figsize=(12, 8))
    plt.title('Feature Importances for Restaurant Rating Prediction')
    plt.bar(range(min(20, len(importances))), importances[indices[:20]], align='center')
    plt.xticks(range(min(20, len(importances))), [feature_names[i] for i in indices[:20]], rotation=90)
    plt.tight_layout()
    plt.show()

    # Print top 10 features
    print("\nTop 10 Most Important Features:")
    for i in range(min(10, len(feature_names))):
        print(f"{feature_names[indices[i]]}: {importances[indices[i]]:.4f}")

# Actual vs Predicted Ratings
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_rf, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel('Actual Rating')
plt.ylabel('Predicted Rating')
plt.title('Actual vs Predicted Restaurant Ratings')
plt.tight_layout()
plt.show()

# Residuals Analysis
residuals = y_test - y_pred_rf
plt.figure(figsize=(10, 6))
plt.scatter(y_pred_rf, residuals, alpha=0.5)
plt.hlines(y=0, xmin=y_pred_rf.min(), xmax=y_pred_rf.max(), colors='r', linestyles='--')
plt.xlabel('Predicted Rating')
plt.ylabel('Residuals')
plt.title('Residual Analysis')
plt.tight_layout()
plt.show()

# Compare models
models = ['Linear Regression', 'Random Forest']
mse_values = [mse_lr, mse_rf]
r2_values = [r2_lr, r2_rf]
rmse_values = [np.sqrt(mse_lr), np.sqrt(mse_rf)]

# Create comparison table
comparison_df = pd.DataFrame({
    'Model': models,
    'MSE': mse_values,
    'RMSE': rmse_values,
    'R-squared': r2_values
})

print("\nModel Comparison:")
print(comparison_df)

# Determine best model
best_model_idx = np.argmax(r2_values)
print(f"\nBest performing model: {models[best_model_idx]}")
print(f"With R-squared value: {r2_values[best_model_idx]:.4f}")