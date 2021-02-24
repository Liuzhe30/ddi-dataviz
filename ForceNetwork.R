library(dplyr)

# load data
setwd("D:/GitHub/ddi-dataviz/")
pd1 <- read.csv("abacavir-demo/abacavir_pd1.csv",head=T,sep=",")
pd2 <- read.csv("abacavir-demo/abacavir_pd2.csv",head=T,sep=",")

drugid1 <- pd1['X0']
drugid2 <- pd1['X1']
rank <- pd1['X2']

MisLinks <- cbind(drugid1, drugid2, rank)
print(MisLinks)

drugname <- pd2['X0']
label_class <- pd2['X1']
label_size <- pd2['X2']
MisNodes <- cbind(drugname, label_class, label_size)
print(MisNodes)

#install.packages("networkD3")
library("networkD3")
# Plot
forceNetwork(Links = MisLinks, Nodes = MisNodes,
             Source = "X0", Target = "X1",
             Value = "X2", NodeID = "X0",
             Group = "X1", opacity = 1,
             width = 1000,
             height =1000,zoom = T,
             bounded=T,legend=T,
             Nodesize = 'X2',
             opacityNoHover = 1, charge=-50,
             radiusCalculation = JS(" d.nodesize"),
             fontSize = 12,arrows = F)

library(magrittr)

forceNetwork(networkData) %>%
  saveNetwork(file = 'Net1.html')

