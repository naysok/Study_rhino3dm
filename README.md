# Study_rhino3dm  


CPython x rhino3dm で UserText を読み書きする最小限のサンプル。  
Point 型に、UserText つけられなそうだったので、PointCloud 型で。


## UserText  

- rhino3dm.ObjectAttributes -> UserString  
  - こちらが普段使っていわゆる UserText っぽい。  

- rhino3dm.CommonObject -> UserString  
  - ライノからアクセスする方法がわからない  



```python
### rhino3dm.CommonObject -> UserString

### Define Geometry
pt = rhino3dm.Point(rhino3dm.Point3d(1, 2, 3))

### Define UserText
pt.SetUserString("TEST_KEY", "TEST_VALUE")

```




## Ref  

- rhino3dm (github)  
  - [https://github.com/mcneel/rhino3dm](https://github.com/mcneel/rhino3dm)  

- Rhino3dm.js の使い方 〜HTML編〜 (hiron-san)  
  - [https://hiron.dev/articles/Intro-Rhino3dm-js-in-html](https://hiron.dev/articles/Intro-Rhino3dm-js-in-html)  