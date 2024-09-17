# DS.v3.1.3.5

# Spotify Top 50 Tracks of 2020 Analysis

This project analyzes the Spotify Top 50 Tracks of 2020 dataset to understand what makes a hit song. By examining various attributes such as danceability, loudness, energy, and duration, the project seeks to uncover trends and patterns in popular music.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset Information](#dataset-information)
- [Objectives](#objectives)
- [Data Cleaning and Preparation](#data-cleaning-and-preparation)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Correlation Analysis](#correlation-analysis)
- [Key Insights](#key-insights)
- [Installation and Usage](#installation-and-usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## Project Overview
This project uses the Spotify Top 50 Tracks of 2020 dataset to perform data analysis and extract insights about popular music. It examines features such as:
- Danceability
- Loudness
- Energy
- Duration
- Acousticness

The analysis focuses on comparing these attributes across different music genres, including Pop, Hip-Hop/Rap, Dance/Electronic, and Alternative/Indie.

## Dataset Information
The dataset includes information about the top 50 most popular tracks on Spotify in 2020. Each track is associated with several audio features and metadata, such as:
- Track name
- Artist
- Genre
- Duration (in milliseconds)
- Popularity
- Danceability, energy, loudness, acousticness, and other musical features

### Source
The dataset is publicly available and can be downloaded from sources such as [Kaggle](https://www.kaggle.com/), or other open datasets. It is originally provided by Spotify.

## Objectives
The primary objectives of this analysis include:
1. Identify which artists and genres dominated the Top 50 list.
2. Compare the danceability, loudness, and acousticness scores across different genres.
3. Find the longest and shortest tracks.
4. Perform correlation analysis to identify relationships between musical features.
5. Understand the characteristics that are common in popular tracks.

## Data Cleaning and Preparation
Several data cleaning steps were performed to ensure the dataset was ready for analysis:
- **Handling Missing Values**: Missing values in the dataset were filled or dropped based on the importance of the data.
- **Removing Duplicates**: Duplicate records were identified and removed.
- **Outlier Treatment**: Outliers in numerical features such as `duration_ms` were handled using statistical methods.
- **Data Type Correction**: Ensured proper data types for features such as `duration_ms` (converted to integers).

## Exploratory Data Analysis (EDA)
The project performed several exploratory analyses, including:
- Genre distribution analysis.
- Identifying which artists had multiple tracks in the top 50.
- Comparing features like danceability and loudness across genres.

## Correlation Analysis
A correlation matrix was computed to find relationships between the various audio features, identifying strong positive or negative correlations among:
- Danceability
- Energy
- Acousticness
- Loudness

## Key Insights
Some key findings from the analysis include:
- **Longest Track**: The longest track in the Top 50 list is "Safaera" with a duration of 295,177 milliseconds.
- **Danceability**: Danceability scores vary significantly between genres, with Dance/Electronic tracks generally having higher scores.
- **Loudness**: Pop and Hip-Hop/Rap tracks tend to have louder audio levels compared to Alternative/Indie tracks.
- **Artist Dominance**: Some artists had multiple tracks in the Top 50 list.

## Installation and Usage
To run this project on your local machine, follow these steps:

### Prerequisites
- **Python 3.x** installed on your system.
- Required Python libraries: `pandas`, `numpy`.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/spotify-top-50-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd spotify-top-50-analysis
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
To run the analysis:
1. Open the Jupyter Notebook:
   ```bash
   jupyter notebook SpotifyAnalysis.ipynb
   ```
2. Follow the steps in the notebook to load the dataset and perform the analysis.

## Technologies Used
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical computations.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or report issues to improve this project.
