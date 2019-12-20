df_1<-read.csv("~/bia678/markov chain/a2/df_markov_client270.csv")

library(markovchain)

sequence_1=df_1$building
markov_1<-markovchainFit(sequence_1,method = "mle", byrow = TRUE, nboot = 10,laplacian=0)
tmA<-markov_1$estimate
tmA
library(diagram)
plot(tmA)

# initialState<-c(0,0,0,0,0,0,1,0,0)
# steps<-2
# finalState<-initialState*tmA^steps #using power operator
# finalState
# 
tmA
# Create the transition matrix
transition_mtrx <- tmA
# Create a table with the transitions
htmlTable(transition_mtrx, title = "Transitions", ctable = TRUE)
transitionPlot(transition_mtrx)
