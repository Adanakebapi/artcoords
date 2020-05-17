# Art-Coords
Art-Coords is like to orthogonal coordinate system. The differences are: It's in python, not math. There is only integers.  
You can change `rule` function to do what you want.  
  
**NOTE:** The squares in blue have 0 variable. Example:  
![ExampleAboutBlue](/whatisblue.png)


Zoomed Photo of Plot Graph:  
![Zoomed](/graphzoomed.png)
  
* Example 1: Ring  
```python
def rule(x,y):
  return 10000 < int(x**2+y**2) < 15000
```
![Ring](/graphring.png)
  
* Example 2: Symbol  
```python
def rule(x,y):
  return (10000 < int(x**2+y**2) < 15000) and ((x < -20) or (x > 20)) or (int(x**2+y**2) < 1000) or ((-10 < y < 10) and (-112 < x < 112))
```
![Symbol](/graphsymbol.png)
  
* Example 3: :thinking:  
```python
def rule(x,y):
  return (100 < (x**2+y**2)**0.5 < 110) or (((x+30)**2*1.5+(y-40)**2)**0.5 < 15) or (((x-30)**2*1.5+(y-40)**2)**0.5 < 15) or (((x+35)**2+(y+75)**2)**0.5 < 40) or ((-12 < x-y*0.5+25 < 0) and (-65 < y < -10)) or ((-22 < x-y*2.5-70 < 0) and (-45 < y < 0) and (x < 20)) or ((((x+5)**2+(y+10)**2*5)**0.5 < 20) and (not (((x+5)**2+(y+16)**2*5)**0.5 < 20))) or ((((x+30)**2+(y-70)**2*5)**0.5 < 20) and (not (((x+30)**2+(y-64)**2*5)**0.5 < 20))) or ((((x-35)**2+(y-51)**2*5)**0.5 < 20) and (not (((x-35)**2+(y-45)**2*5)**0.5 < 20)))
```
![Thinking](/graphthinking.png)
