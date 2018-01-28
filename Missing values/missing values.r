#Leer el dataset
dataset = read.csv('prestamos.csv')

#Ver valores nulos
summary(dataset)

#0.Decodificar los NA
dataset$Sexo[dataset$Sexo == ""] = NA
dataset$Casado[dataset$Casado == ""] = NA


#1.Eliminar valores nulos
dataset=na.omit(dataset)


#2.Inputar valores nulos
dataset$Sexo = ifelse(is.na(dataset$Sexo), as.character(mode(dataset$Sexo)), as.character(dataset$Sexo))
dataset$Casado = ifelse(is.na(dataset$Casado), as.character(mode(dataset$Casado)), as.character(dataset$Casado))
dataset$CantidadPrestamo = ifelse(is.na(dataset$CantidadPrestamo), mean(dataset$CantidadPrestamo, na.rm=TRUE), dataset$CantidadPrestamo)
dataset$Plazo = ifelse(is.na(dataset$Plazo), mean(dataset$Plazo, na.rm=TRUE), dataset$Plazo)

