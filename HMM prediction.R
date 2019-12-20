library(HMM)
library(markovchain)

setwd("C:/Users/dell/Documents/bia678/markov chain/a1")
listcsv <- dir(pattern = "*.csv")
emission_df <- list()
for (k in 1:length(listcsv))
{emission_df[[k]] <- read.csv(listcsv[k])}


setwd("C:/Users/dell/Documents/bia678/markov chain/a2")
listcsv_1 <- dir(pattern = "*.csv")
sequence_df <- list()
for (j in 1:length(listcsv))
{sequence_df[[j]] <- read.csv(listcsv_1[j])}
h1=0
length(listcsv)
listcsv[m]
for (m in 1:268)
{
  df_1<-sequence_df[[m]]
  sequence_1=df_1$building
  observations=df_1$observation[(length(sequence_1)-7):length(sequence_1)]
  states_initail=df_1$building[(length(sequence_1)-7):length(sequence_1)]
  markov_1<-markovchainFit(sequence_1,method = "mle", byrow = TRUE, nboot = 10,laplacian=0)
  transProb<-markov_1$estimate
  df_2<-emission_df[[m]]
  df_2[is.na(df_2)] <- 0
  rownames(df_2) <- df_2$X
  df_2<-subset(df_2, select=-c(X))
  emissProb=as.matrix(df_2)
  elements=colnames(df_2)
  states=rownames(df_2)
  
  
  
  startProbs_2=matrix(0,nrow=1,ncol=length(states))
  colnames(startProbs_2) <- rownames(df_2)
  for (q in 1:length(states)){ 
    if (states[q]==states_initail[1]){startProbs_2[1,q]=1}
  }
  
  hmm <- initHMM(States = states, 
                   Symbols = elements,
                   transProbs=transProb,
                   emissionProbs = emissProb,
                 startProbs=startProbs_2)
  #print(hmm)
  # # Calculate Viterbi path
  viterbi = viterbi(hmm,observations)
  states_initail<- lapply(states_initail, as.character)
  if ((viterbi[2]==states_initail[2]) 
       & (viterbi[3]==states_initail[3])
      & (viterbi[4]==states_initail[4])
      & (viterbi[5]==states_initail[5])
      & (viterbi[6]==states_initail[6])
      )
    {h1=h1+1}

}


cat('hmm prediction accuracy',h1/length(listcsv))