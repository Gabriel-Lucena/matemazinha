#ifndef DERIVATE_H
#define DERIVATE_H

#include "../function/function.h"

double derivative(double x, double a, double b, double interval)
{
  if (interval)
  {
    double y = linear(x, a, b);

    double taxa = (linear(x + interval, a, b) - linear(x, a, b)) / (interval);

    return taxa;
  }

  double y = a * x + b;

  double rate = (linear(x + 0.001, a, b) - linear(x, a, b)) / (0.001);

  return rate;
}

#endif