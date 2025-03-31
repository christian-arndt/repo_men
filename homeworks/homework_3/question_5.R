library(tidyverse)
library(ggcorrplot)
require(psych)
library(lavaan)
library(lavaanPlot)
library(ggplot2)
library(knitr)
library(xtable)


setwd('/Users/chris/Documents/Behavioral Data Science/repository/repo_men/homeworks/homework_3')


# Read in data
data = read.table("data/personality_data.csv", header = T , sep= ";")

# Get only ABCDE subscale data
data_selections = data %>% select(matches("^[ABCDE]"),  -c("age", "accuracy", "country", "elapsed"))


## Next, we remove participants with suspicious elapsed time
median_elapsed = median(data$elapsed, na.rm = T)
mad_elapsed = median(abs(data$elapsed - median_elapsed), na.rm = T)

mask = data$elapsed < median_elapsed + 1.5*mad_elapsed & 
  data$elapsed > median_elapsed - 3*mad_elapsed

data_selections = data_selections[mask,]


# Ensure no missings present
# 0s are equivalent to NA values for these columns
data_selections[data_selections == 0] = NA

# Impute NAs
for (i in 1:ncol(data_selections)) {
  data_selections[is.na(data_selections[,i]), i] = mean(data_selections[,i], na.rm = TRUE)
}

# Ensure imputation worked
sum(is.na(data_selections))


# Generate and inspect heatmap of correlation matrix
corr = cor(data_selections)
ggcorrplot(corr, lab = F)


# Determine the number of factors: first, do a PCA and scree plot

# Do pca (we don't need to do this to get the eigenvalues but it's easy)
pca = prcomp(data_selections)

# Extract the eigenvalues from the PCA object
eigenvalues = pca$sdev^2

# Create a scree plot
plot(eigenvalues, type = "b",
     xlab = "Principal Component",
     ylab = "Eigenvalue")


# We want to do 5 factor factor analysis
fit = factanal(data_selections, 5)

# Extract the factor loadings
loadings_df = as.data.frame(unclass(fit$loadings))
dim(loadings_df)

# Set appropriate column names (F1, F2, F3, F4, F5)
colnames(loadings_df) = c("F1", "F2", "F3", "F4", "F5")

xtable(loadings_df)


# Extract communalities
communalities_df = as.data.frame(rowSums(loadings_df ^ 2))
xtable(communalities_df)
