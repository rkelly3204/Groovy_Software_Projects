install.packages("corrplot")
install.packages("ggplot2")
install.packages("tidyverse")
install.packages("randomForest")
install.packages("e1071")
install.packages("dummies")
install.packages("dplyr")

# libraries
library(e1071)
library(ggplot2)
library(corrplot)
library(readr)
library(dplyr)
library(MASS)
library(ggplot2)
library(rpart)
library(randomForest)
library(dummies)

#--------------------------------------------
#READ:
# I wrote out all the regression code, You will
#have to figure out what y and x variables that
#are needed. Simple replace varY for the y variable,
#and varX for the X variables
#--------------------------------------------


#Load Dataset and remove "NA"
#mydata = whole dataset SentinelEventData.csv
#--------------------------------------------
mydata <- read_csv("C:/Users/Ryan_Kelly/Desktop/SentinelEventData.csv")
mydata <- na.omit(mydata)
#--------------------------------------------

dumm_data <- data.frame(mydata$'Gender',mydata$'Race',mydata$'Insured',mydata$'ED_CC')
str(dumm_data)

#Create a new dataset with dummy variables
dumm_data <- dummy.data.frame(dumm_data)
dumm_data <- na.omit(dumm_data)

#factored Variables
#--------------------------------------------
mydata$'Deceased' <- as.factor(mydata$'Deceased?')
mydata$'Race'<- as.factor(mydata$'Race')
mydata$'Insured'<-as.factor(mydata$'Insured')
mydata$'Ethnicity'<-as.factor(mydata$'Ethnicity')
mydata$'ED_CC'<-as.factor(mydata$'ED_CC')
mydata$'Level_of_Care'<-as.factor(mydata$'Level_of_Care')
mydata$'Trauma_Activation'<-as.factor(mydata$'Trauma_Activation')
mydata$'RRT'<-as.factor(mydata$'RRT')
mydata$'Code99'<-as.factor(mydata$'Code99')
mydata$'Intubated'<-as.factor(mydata$'Intubated')
#--------------------------------------------
colnames(mydata[4])<-"Deceased"
factoredData <- subset(mydata, select = c("Deceased?","Race","Insured","Ethnicity","ED_CC","RRT","Code99")) #Select Dummy Vars

RegData <- subset(mydata,select = c("ED_LOS_hrs","Age","ED_SBP","ED_MAP","ED_SpO2",
                                    "ED_O2Source","ED Temp","24hr_SBP","24hr_DBP","24hr_MAP","24hr_HR","24hr_RR","24hr_SpO2",
                                    "24hr_Temp","48hr_Temp","48hr_SBP","48hr_DBP","48hr_MAP","48hr_HR","48hr_RR","48hr_SpO2",
                                    "Latest_SBP","Latest_DBP","Latest_MAP","Latest_HR","Latest_RR","Latest_SpO2","Latest Temp"))
RegData$dumm_data <- dumm_data
explore$RegData <-RegData

#Exploration
#--------------------------------------------
summary(mydata)
#--------------------------------------------

#Visulaizations 
#ED_CCT = ED_CC Table
#EthT = Ethnicity Table
#RT = Race Table
#LoCT = Level_of_Care Table
#--------------------------------------------
ggplot()

#ED_CC
ED_CCT <- table(mydata$'ED_CC')
barplot(ED_CCT)

#Ethnicity
EthT <- table(mydata$'Ethnicity')
barplot(EthT)

#Race
RT <- table(mydata$'Race')
barplot(RT)

#Level_of_Care
LocT <- table(mydata$'Level_of_Care')
barplot(LocT)


#---------------------------------------------
# Regression Testing
#---------------------------------------------
#Univariate Regression
#Place Y variable in varY and variable X in VarX1
model1 <- lm(as.numeric(ED_LOS_hrs) ~ ED_SBP+ED_DBP+ED_MAP+ED_RR , data=regdata) 
summary(model1)

#Multivariate Linear Regression
#------------------------------------
#Place Y variable in varY and variable X in VarX1
#and so on for varX2-3
model3 <- lm(Time_of_Event_After_ED_Discharge_hrs ~ ED_SBP+ED_DBP+ED_MAP+ED_RR,data=mydata)
summary(model3)

#Stepwise Regression
#------------------------------------
#Compares all Vars to each other to get the best r equation
#goes both ways. Place variable in for varY to get a result
model5 <- lm(Time_of_Event_After_ED_Discharge_hrs ~., data=explore)
step <- stepAIC(model5,direction = "both")
summary(step)

#Mupltiple Linear Regression Example
#------------------------------------
# Splits the data set 80/20 better performance for 
#future data, Insert y variable for varY and 
# X variable in for varx1-3
selec <- sample(1:nrow(RegData),.8*nrow(RegData))
Training <- RegData[selec, ] #splits into a training set
Testing <- RegData[-selec, ] #splits into a test set

MD.lm <-lm(as.numeric(ED_LOS_hrs) ~.,data=Training)
summary(MD.lm) #prints the results

#Model Validation
#------------------------------------
#Calcualte RMSE for the Training Data
# Insert Y variable for varY
preTr <- predict(MD.lm, newdata = Training)
rmseTr <- sqrt(sum((Training$Time_of_Event_After_ED_Discharge_hrs-preTr)^2)/nrow(Training))
rmseTr

#Calculate RMSE for the Testing Data
preTe <- predict(MD.lm, newdata=Testing)
rmseTe <- sqrt(sum((Testing$Time_of_Event_After_ED_Discharge_hrs-preTe)^2)/nrow(Testing))
rmseTe

#Plotting the Residuals
#------------------------------------
#Insert y variable for varY and 
# X variable in for varx1-3
MD.lm <- lm(Time_of_Event_After_ED_Discharge_hrs~RRT+ED_SpO2+Latest_MAP,data = Training)
plot(residuals(MD.lm))
abline(h=0,col="red")

#Diagnostic Plots for Residuals
#------------------------------------
par(mfcol =c(2,2))
plot(MD.lm)

#Logistic Regression using pima
#------------------------------------
#Insert y variable for varY and 
# X variable in for varx1-3
model6 <- glm(mydata.ED_CC8 ~ .,data=dumm_data,family = binomial(link="logit"))
summary(model6)

model7 <- glm(Time_of_Event_After_ED_Discharge_hrs~., data=RegData,family = binomial(link="logit"))
summary(model7)

#First partition the data into 80% training and 20% testing data
selec <- sample(1:nrow(RegData),.8* nrow(RegData))
Training <- RegData[selec,]
Testing <- RegData[-selec,]

#Next, develop logistic regression model using Training data with all 
#independent variables included
MD.lr <- glm(varY~., data=Training, family=binomial(link="logit"))
summary(MD.lr)

#Model Validation for LR: Confusion Matrix
#------------------------------------
#Insert y variable for varY and 
MD.lr <-glm(varY~.,data=Training, family = binomial(link="logit"))

#Create predicted values of test in testing data
preTe<-predict(MD.lr,newdata = Testing, type="response")

#predictions are probabilites recorded as "1" if prob >0.5,"0" otherwise
preTe_10 <- ifelse(preTe>.5,1,0)

table(Testing$varY, preTe_10)

#Regression Tree
#------------------------------------
#First partition the data into 80% training and 20% testing data
selec <- sample(1:nrow(RegData),.8*nrow(RegData))
Training <- RegData[selec, ]
Testing <- RegData[-selec, ]

nrow(Training)
nrow(Testing)

#Devloping a Regression Tree
#------------------------------------
#Insert y variable for varY and 
# X variable in for varx1-3
MD.rp<-rpart(Time_of_Event_After_ED_Discharge_hrs~RRT+ED_SpO2+Latest_MAP, cp=0, data=Training)

print(MD.rp)

#Prunes the tree
MD.rp<-rpart(Time_of_Event_After_ED_Discharge_hrs~RRT+ED_SpO2+Latest_MAP, cp=.01, data=Training)
summary(MD.rp)

#Plots the Tree
plot(MD.rp, uniform = T)
text(MD.rp, use.n = T,cex=.8,all=T,minlength = 9, xpd=T)

#Evaluates the model performance in Testing data using RMSE
preTr<-predict(MD.rp, newdata = Training)
rmseTr<-sqrt(sum((Training$Time_of_Event_After_ED_Discharge_hrs-preTr)^2)/nrow(Training))

preTe<-predict(MD.rp, newdata = Testing)
rmseTe<-sqrt(sum((Testing$varY-preTe)^2)/nrow(Testing))

rmseTr
rmseTe

#Random Forest: WorkForce
#------------------------------------
#Insert y variable for varY and 
# X variable in for varx1-3
MD.bag<-randomForest(Time_of_Event_After_ED_Discharge_hrs~RRT+ED_SpO2+Latest_MAP,data=Training, ntree=500,mtry=3,
                     maxnodes=7)
plot(MD.bag, uniform = T)
text(MD.bag, use.n = T,cex=.8,all=T,minlength = 9, xpd=T)

preTr2<-predict(MD.bag,newdata=Training)
rmseTr2 <- sqrt(sum((Training$Time_of_Event_After_ED_Discharge_hrs-preTr2)^2)/nrow(Training))

preTe2<-predict(MD.bag, newdata=Testing)
rmseTe2<-sqrt(sum((Testing$Time_of_Event_After_ED_Discharge_hrs-preTe2)^2)/nrow(Testing))

rmseTr2
rmseTe2 

#SVM: Support Vector Machine
#------------------------------------

svmfit = svm(Time_of_Event_After_ED_Discharge_hrs~RRT+ED_SpO2+Latest_MAP,data=RegData,kernel="linear",cost = 10, scale = FALSE)
summary(svmfit)

#--------------------------------------------
#Correlation Testing through the numeric data
#corData = Numeric Values converted into corllation values 
#--------------------------------------------
corData <- subset(mydata, select = c("ED Temp","24hr_Temp","48hr_Temp","Latest Temp")) #Numeric Vars
corData <- cor(corData)
corrplot(corData, type = "upper")

#mat : is a matrix of data
# ... : additonal passed in vars
#Creates a Matrix of Pvalues for the selected Vars
cor.mtest <- function(mat, ...){
  mat <- as.matrix(mat)
  n <- ncol(mat)
  p.mat <- matrix(NA, n, n)
  diag(p.mat)<- 0
  for (i in 1:(n - 1)){
    for(j in (i + 1)){
      tmp <- cor.test(mat[, i], mat[, j], ...)
      p.mat[i, j] <- p.mat[j, i] <- tmp$p.value
    }
  }
  colnames(p.mat) <- rownames(p.mat) <- colnames(mat)
  p.mat
}

p.mat <- corData
head(p.mat)


#Cluster analysis
#------------------------------------
