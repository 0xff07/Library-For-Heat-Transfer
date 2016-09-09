>大部分是用Python寫成，只是個方便寫作業(code寫完複製貼適當計算過程)以及帶大抄的東西（雖然考試不能帶電腦）。<br/>
>這份code並沒有針對精度去做優化，基本上就是維基上有什麼公式就暴力帶入。比較像是把Python直譯器當做高級的計算機用。但是就交作業的程度來說，大概堪用（不知道為什麼會有作業能忍受5%的誤差）。<br/>
>日後可能會加入一些解微分方程的數值方法，甚至是PDE解法。不過，前來說不是很想仰賴NumPy(想想Linux系統以外安裝NumPy是多麻煩)，所以PDE大概得等上一段時間吧。<br/>

##函數說明
###fin.py
* UNIFORM_FIN 物件，表示截面均相同，處於穩態且沒有heat source的鰭片。
* k : 熱導係數
* h : 對流係數
* L : 鰭片長度
* P : 鰭片周長
* A : 鰭片截面積
* T0: Base溫度
* Too: 無窮遠處溫度（熱對流用)
* m : sqrt(hP/Ak)，解ODE用的參數。init時自動算好
* M : sqrt(hPkA)，解ODE用參數。init時自動算好
* UNIFORM_FIN(k, h, L, P, A, T0, Too)的順序可以用「卡懶趴」 + 兩端溫度 來記憶。
* T(x, type, Tl = 0)：輸入 x 與邊界條件種類，位置x的溫度。type 必須輸入邊界條件的名稱(是個字串)。可使用的種類有4種，'convection', 'adiabatic', 'constant temperature', 'infinite'. 只有'constant temperature'需要輸入給定的溫度邊界條件Tl，其餘Tl可忽視。
* QRate(type, Tl = 0)：輸入邊界條件種類，輸出熱流率。因為是steady state且沒有heat source所以處處相等，不需要輸入位置，但是若邊界條件為'constant temperature'則需輸入邊界溫度Tl。
* getResistance(type)：輸入邊界條件種類，輸出熱阻值。
* 預計加入函數：fin effectness, fin efficiency, 多個fin並列的效能, 一些常用形狀的fin的經驗公式, fin equation solver（至少是某些特定狀況下的）。

