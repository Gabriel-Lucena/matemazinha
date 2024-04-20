#ifndef INTEGRAL_H
#define INTEGRAL_H

/**
 * Integrate the function f(x) = ax + b.
 *
 * @param inferior Inferior limit of the integral.
 * @param superior Superior limit of the integral.
 * @param a The a value.
 * @param b The b value.
 * @param interval dx's size. Default is 0.0001.
 * @return The integral value.
 */
double integral(double inferior, double superior, double a, double b, double interval)
{
  if (interval)
  {
    double y;
    double x = inferior;
    double area = 0;

    while (x < superior)
    {
      y = a * x + b;
      area += interval * y;
      x += interval;
    }

    return area;
  }

  double y;
  double x = 0;
  double area = 0;

  while (x < 1)
  {
    y = x;
    area += 0.0001 * y;
    x += .0001;
  }

  return area;
}

#endif