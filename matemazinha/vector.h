#ifndef VECTOR_H
#define VECTOR_H

#include "vector.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct
{
  double i;
  double j;
  double k;
} Vector;

double *vectorToArray(Vector vector)
{
  double *array = (double *)malloc(3 * sizeof(double));

  if (array == NULL)
  {
    return NULL;
  }

  array[0] = vector.i;
  array[1] = vector.j;
  array[2] = vector.k;

  return array;
}

void listVector(Vector vector)
{
  printf("\n%lf ^ i + %lf ^ j + %lf ^ k\n", vector.i, vector.j, vector.k);
}

void listReal(double real)
{
  printf("\n%lf \n", real);
}

Vector sum(Vector vectorA, Vector vectorB)
{
  Vector vector = {vectorA.i + vectorB.i, vectorA.j + vectorB.j, vectorA.k + vectorB.k};
  return vector;
}

Vector productByReal(Vector vector, double value)
{
  Vector vectorProduct = {vector.i * value, vector.j * value, vector.k * value};
  return vectorProduct;
}

double absoluteValue(Vector vector)
{
  double absoluteValue = sqrt(vector.i * vector.i + vector.j * vector.j + vector.k * vector.k);
  return absoluteValue;
}

Vector normalize(Vector vector)
{
  double value = absoluteValue(vector);
  Vector normalizedVector = {vector.i / value, vector.j / value, vector.k / value};
  return normalizedVector;
}

double scalarProduct(Vector vectorA, Vector vectorB)
{
  double scalarProduct = vectorA.i * vectorB.i + vectorA.j * vectorB.j + vectorA.k * vectorB.k;
  return scalarProduct;
}

void listScalarProduct(Vector vectorA, Vector vectorB)
{
  double scalarProduct = vectorA.i * vectorB.i + vectorA.j * vectorB.j + vectorA.k * vectorB.k;
  listReal(scalarProduct);
}

Vector vectorialProduct(Vector vectorA, Vector vectorB)
{
  double i = vectorA.j * vectorB.k - vectorA.k * vectorB.j;
  double j = vectorA.k * vectorB.i - vectorA.i * vectorB.k;
  double k = vectorA.i * vectorB.j - vectorA.j * vectorB.i;

  Vector vectorialVector = {i, j, k};
  return vectorialVector;
}

void listVectorialProduct(Vector vectorA, Vector vectorB)
{
  Vector vectorialProductResult = vectorialProduct(vectorA, vectorB);
  listVector(vectorialProductResult);
}

#endif