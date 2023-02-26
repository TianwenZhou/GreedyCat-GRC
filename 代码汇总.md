``# 综合编程复习
## MFC操作
### 创建
1. 起名字（首字母大写）
2. 不勾选“创建目录”
3. 选“基于对话框”
4. 取消勾选“关于框”
### 删除
1. .vs文件夹
2. Debug文件夹
3. x64文件夹
4. My Advisor Results文件夹
5. *.aps文件夹
6. 演示、联系要求等
### 使用
1. 打开“解决方案管理器”窗口
2. 打开“资源管理器”窗口
3. 打开Dialog-工具箱
4. 注意可能删除的最大化、最小化按钮，确定、取消按钮
5. DIALOG对话框-属性-Caption-修改名称
## 编程操作
- 定义变量：在头文件xxxDlg.h中定义变量
- 在xxxDlg.cpp文件OnInitDialog()中初始化变量，赋初值
- 结构体变量
- 或：|| 且：&&
 ```
struct DATA
{
CString name;
CString year;
CString place;
int number;
int total;
} data[4],curData;
```
- 清空：
 `Invalidate(true); `
 - 弹窗提示：
`MessageBox(TEXT("请输入一个正数"))`
## 工具箱操作
- 拖拽添加工具-右键添加事件处理程序-右键修改名称
- 下拉列表框-属性-行为 sort=false
- 单选框 radio button 根据要求杂项-group 设置 true/false
## 画图类代码
### 坐标运算
- 左上角最小，右下角最大
### 画笔类变量
![](%E4%BB%A3%E7%A0%81%E6%B1%87%E6%80%BB_md_files/01375170-b57f-11ed-8327-4193e6e43d4a_20230226104101.jpeg?v=1&type=image&token=V1:8VCX9AmNlwOAwXEwGPl2BZNBUTkLiB8-fchp-AO8hyc)
```
pen.CreatePen(int nPenStyle,int nWidth,color)
```
### 画点
```
	int i, j;
	CClientDC dc(this); // 获得对话框的客户区设备上下文
	// 画直角三角形
	for (j = 10; j <= 100; j++) // 行
	{
		for (i = 10; i <= j; i++) // 列
		{
			dc.SetPixel(i, j, RGB(255, 0, 0));  // 在（i，j）画红点
		}
	}
```
### 画线
```
CClientDC dc(this); // 获得对话框的客户区设备上下文
CPen pen; // 定义画
// 创建画笔（实线、宽度为1、颜色为黄）
pen.CreatePen(PS_SOLID, 5, RGB(255, 255, 0));
// 加载画笔
dc.SelectObject(&pen); // 设置设备dc的画笔为pen
// 画线
dc.MoveTo(400, 10); // 将画笔移动到新的起点
dc.LineTo(500, 10); // 用画笔画一条新的线
// 删除画笔
pen.DeleteObject();
```
### 画刷
功能：画笔作为边框，画刷进行填充
```
	CClientDC dc(this); // 获得对话框的客户区设备上下文
	CPen pen; // 定义画笔	
	//画笔画轮廓 画刷填充颜色	 
	CBrush brush; // 定义画刷
	pen.CreatePen(PS_SOLID, 3, RGB(255, 0, 0)); // 创建画笔：红色	
	dc.SelectObject(pen); // 加载画笔	
	brush.CreateSolidBrush(RGB(0, 0, 255));  // 创建画刷：蓝色	
	dc.SelectObject(&brush); // 加载画刷	
	dc.Rectangle(50, 200, 150, 300); // 画正方形	
	pen.DeleteObject(); // 删除画笔	
	brush.DeleteObject(); // 删除画刷
```
### 画矩形函数：
`Rectangle(x1,y1,x2,y2)：画矩形，左上角为(x1,y1)，右下角为(x2,y2)`
或
```
dc.FillSolidRect(40, 40, 300, 300, RGB(240, 240, 240))//也可以用于擦除一块矩形区域
```
### 画椭圆
```
	CClientDC dc(this);//获取客户区
	CBrush brush;//定义画刷
	int r;//圆的半径
	int x ;//将x坐标提取出来
	int y;//将y坐标提取出来
	r = (rand() % 41) + 10;//随机生成圆的半径且在10-50之间
	brush.CreateSolidBrush(RGB(0,0,0));//创建画刷
	dc.SelectObject(&brush);//加载画刷brush到设备dc
	dc.Ellipse(x - r, y - r, x + r, y + r);//画圆,矩形的内切椭圆
	brush.DeleteObject();//删除画刷
```
`dc.Ellipse(x1,y1,x2,y2): 画左上角(x1,y1)，右下角(x2,y2)矩形的内接椭圆`
### 输出文字
```
CClientDC dc(this);//获取客户区
dc.SetTextColor(RGB(255,0,0));//设置文字颜色
dc.SetBkColor(RGB(255,0,0));//设置背景颜色
CFont font;//定义字体
font.CreatePointFont(400, L"宋体");//创建字体
dc.SelectObject(&font);//绑定字体
dc.TextOutW(110, 50, L"输出一段文字");//输出字符串
font.DeleteObject();//删除字体]
```
### 调用调色板
```
CColorDialog dlg;//定义颜色对话框
COLORREF color;//定义画笔的颜色
if (point.x > 50 && point.x < 100 && point.y>50 && point.y < 100)//////指定位置(point.x,point.y为鼠标点击消息)
{
	dlg.DoModal();//打开颜色对话框
	color = dlg.GetColor();//获取颜色
}
```
通过上述方法，可以给color变量赋值，进而调整绘图的颜色，而变量color是一个COLORREF型变量，需要在头文件中进行**初始化**方可使用。
### 显示颜色值
```
CString str;//定义字符串
COLORREF color;//定义画笔的颜色
str.Format(L"0x%06x", color);//将int型颜色值转化为十六进制字符串
dc.TextOutW(110, 50, str);//输出字符串
```
### 画刷橡皮擦
```
CClientDC dc(this);//加载画刷
dc.SelectObject(&brush);//加载画刷brush到设备dc
//设置橡皮擦效果
dc.SetROP2(R2_NOTXORPEN);//异或运算
//擦除旧色块
dc.Rectangle(pStart.x, pStart.y, pEnd.x, pEnd.y);//画色块
//更新终点坐标
pEnd = point;
//画新色块
dc.Rectangle(pStart.x, pStart.y, pEnd.x, pEnd.y);//画色块
```
### 画笔橡皮擦
```
CClientDC dc(this);
//加载画笔
dc.SelectObject(&pen);
//设置橡皮擦效果
dc.SetROP2(R2_NOTXORPEN);
//擦除旧线
dc.MoveTo(pStart.x, pStart.y);
dc.LineTo(pEnd.x, pEnd.y);
//更新终点坐标
pEnd = point;
//画新线
dc.MoveTo(pStart.x, pStart.y);
dc.LineTo(pEnd.x, pEnd.y);
```
### 绘制底图（如坐标系等）
在OnPaint()函数中绘制
```
if (IsIconic())
	{
		...
	}
	else
	{
		// 绘制网格线
		CClientDC dc(this);
		int i, j;
		// 画横线
		for (j = 0; j <= 10; j++)
		{
			dc.MoveTo(0, j * 40);
			dc.LineTo(400, j * 40);
		}
		// 画竖线
		for (i = 0; i <= 10; i++)
		{
			dc.MoveTo(i * 40, 0);
			dc.LineTo(i * 40, 400);
		}
```
## 图片类代码
### 方法一：插入资源位图
1. 把图片放在\res文件夹下
2. 资源视图-.rc添加资源-Bitmap-导入
3. 修改位图资源ID
4. 添加图片控件 Picture Control
5. 设置属性Type = Bitmap，关联位图
6. 为Picture Control控件添加变量，类别 = 控件，名称自定
### 在头文件中添加资源位图变量&句柄
```
CBitmap bitmapRed;//红灯图片对象
HBITMAP hBmpRed;//红灯图片对象句柄
CBitmap bitmapYellow;//黄灯图片对象
HBITMAP hBmpYellow;//黄灯图片对象句柄
CBitmap bitmapGreen;//绿灯图片对象
HBITMAP hBmpGreen;//绿灯图片对象句柄
CBitmap bitmapGray;//灰灯图片对象
HBITMAP hBmpGray;//灰灯图片对象句柄
```
### 在OnInitdialog()中进行初始化
```
bitmapRed.LoadBitmapW(IDB_BITMAP_RED);//加载红灯位图到图片对象
hBmpRed = (HBITMAP)bitmapRed.GetSafeHandle();// 获取红灯图片对象句柄
bitmapYellow.LoadBitmapW(IDB_BITMAP_YELLOW);//加载黄灯位图到图片对象
hBmpYellow = (HBITMAP)bitmapYellow.GetSafeHandle();// 获取黄灯图片对象句柄
bitmapGreen.LoadBitmapW(IDB_BITMAP_GREEN);//加载绿灯位图到图片对象
hBmpGreen = (HBITMAP)bitmapGreen.GetSafeHandle();// 获取绿灯图片对象句柄
bitmapGray.LoadBitmapW(IDB_BITMAP_GRAY);//加载灰灯位图到图片对象
hBmpGray = (HBITMAP)bitmapGray.GetSafeHandle();// 获取灰灯图片对象句柄
```
### 显示图片
`picRed.SetBitmap(hBmpRed);`
### 方法二：内存设备上下文
用同样的方式把图片导入到资源文件中，
在xxxDlg.h文件中写入：
```
CBitmap bitmapSmile;//CBitmap对象,用于加载位图//笑脸
CDC memdcSmile;//显示缓存句柄//笑脸
CBitmap bitmapMine;//CBitmap对象,用于加载位图//地雷
CDC memdcMine;//显示缓存句柄//地雷
```
在xxxDlg.cpp文件的OnInitDialog()函数中写入：
```
bitmapSmile.LoadBitmapW(IDB_BITMAP_SMILE);//将位图IDB_BITMAP_SMILE加载到图片对象
memdcSmile.CreateCompatibleDC(&dc);//创建图形缓存句柄
memdcSmile.SelectObject(bitmapSmile);//加载图片到图形句柄
```
### 显示图片
用BitBlt函数
![](%E4%BB%A3%E7%A0%81%E6%B1%87%E6%80%BB_md_files/58a68f70-b5a7-11ed-8327-4193e6e43d4a_20230226152948.jpeg?v=1&type=image&token=V1:Os7AYocxgf1wDoo2zH0x-hrlBnjNAkEl8e7Vg-UNhcw)
`dc.BitBlt(i*40+1, j*40+1, 40, 40, &memdcMine, 0, 0, SRCCOPY)`
```
CClientDC dc(this);
//根据网格内的标志flag显示图片
int i, j;//数组下标
i = point.x / 40;
j = point.y / 40;
if (flag[j][i] == 1)//点击网格的flag为1,显示笑脸
{
dc.BitBlt(i*40+1, j*40+1, 40, 40, &memdcSmile, 0, 0, SRCCOPY);
}
else if (flag[j][i] == 0)//点击网格的flag为1,显示地雷
{
	dc.BitBlt(i*40+1, j*40+1, 40, 40, &memdcMine, 0, 0, SRCCOPY);
}
```
dwRop取值：
![](%E4%BB%A3%E7%A0%81%E6%B1%87%E6%80%BB_md_files/6b7ef910-b5a8-11ed-8327-4193e6e43d4a_20230226153729.jpeg?v=1&type=image&token=V1:IMPPCYGR-G3ceP6FDCHMyrrhsHmdiJNcAOJbRab4HyM)
## 计时器相关操作
### 添加计时器
对话框-消息-WM_TIMER
### 启动计时器
设置计时器1，时长为1000ms
`SetTimer(1, 3000, NULL);`
### 计时器到时
OnTimer()函数
注意：多个计时器共用同一个OnTimer()函数
```
if (nIDEvent == 1) // 计时器1到时
{
// 处理计时器1的事件。。。
}
```
### 停止计时
`KillTimer(1);//停止计时器1	`
## 画会动的正弦曲线
### 生成正弦曲线
```
UpdateData(true);
// 生成正弦曲线：振幅=100，角频率=4，相位=0
for (int i = 0; i <= 498; i++) // 向前平移数据
{
	data1[i] = data1[i + 1];
	data2[i] = data2[i + 1];
}
data1[499] = Amp1 * sin(Ang1 * x * 3.14 / 180 + Pha1); // 生成最后一个数据
data2[499] = Amp2 * sin(Ang2 * x * 3.14 / 180 + Pha2); // 生成最后一个数据
x++;
int x0 = 100, y0 = 300; // 原点坐标
```
### 绘制方法一：直接在dc上绘图
```
// 方法一：直接在dc上擦除再画图
CClientDC dc1(this); // 客户区DC1
CClientDC dc2(this); // 客户区DC2
CClientDC dc3(this); // 客户区DC3
CClientDC dc4(this); // 客户区DC4
CClientDC dc5(this);//获取客户区
CClientDC dc6(this); // 客户区DC6
CClientDC dc7(this); // 客户区DC7
CPen pen1;//定义画笔
CPen pen2;//定义画笔
CPen pen3;//定义画笔
CPen pen4;//定义画笔
CFont font;//定义字体
pen1.CreatePen(PS_SOLID, 1, RGB(255, 0, 0));//创建画笔
pen2.CreatePen(PS_SOLID, 1, RGB(0, 0, 255));//创建画笔
pen3.CreatePen(PS_SOLID, 1, RGB(0, 0, 0));//创建画笔
font.CreatePointFont(100, L"宋体");//创建字体
dc5.SetTextColor(RGB(0, 0, 0));
dc5.SetBkColor(RGB(240, 240, 240));
dc1.SelectObject(&pen1);//将画笔pen加载到设备dc
dc2.SelectObject(&pen2);//将画笔pen加载到设备dc
dc3.SelectObject(&pen3);//将画笔pen加载到设备dc
dc4.SelectObject(&pen3);//将画笔pen加载到设备dc
dc6.SelectObject(&pen3);//将画笔pen加载到设备dc
dc7.SelectObject(&pen3);//将画笔pen加载到设备dc
//////// 擦除区域
dc1.FillSolidRect(0, 180, 15000, 10000, RGB(240, 240, 240));
dc2.FillSolidRect(0, 180, 15000, 10000, RGB(240, 240, 240));
// 画曲线图
dc1.MoveTo(x0, y0); // 从原点开始
dc2.MoveTo(x0, y0); // 从原点开始
dc3.MoveTo(x0 - 20, y0 );//x轴
dc4.MoveTo(x0 , y0+200);//y轴
dc3.LineTo(x0 + 500, y0 );//x轴
dc4.LineTo(x0 , y0-200);//y轴
dc7.MoveTo(x0 - 10, y0-190);//y轴箭头
dc7.LineTo(x0 , y0-200);//y箭头
dc7.LineTo(x0 + 10, y0 - 190);//y箭头
dc6.MoveTo(x0 + 490, y0+10);//x轴箭头
dc6.LineTo(x0 + 500, y0);//x箭头
dc6.LineTo(x0 + 490, y0 - 10);//x箭头
dc5.SelectObject(&font);//绑定字体
dc5.TextOutW(x0-50, y0+10, L"(0,0)");
dc5.TextOutW(x0+490, y0+10, L"x");
dc5.TextOutW(x0-20, y0-200, L"y");
// 画每一个点的连线
int i;
for (i = 0; i < 500; i++)
{
	dc1.LineTo(x0 + i, y0 - data1[i]);
	dc2.LineTo(x0 + i, y0 - data2[i]);
}
```
### 绘制方法二：在内存dc上擦除再画图，再把内存dc复制到dc上

	CClientDC dc(this); // 客户区DC
	CDC memdc; // 内存DC
	CBitmap dcbmp; // 位图

	// 创建与客户区DC兼容的位图
	dcbmp.CreateCompatibleBitmap(&dc, 1000, 1000);
	// 创建与客户区DC兼容的内存DC
	memdc.CreateCompatibleDC(&dc);
	// 在内存DC上加载位图
	memdc.SelectObject(&dcbmp);
	// 内存DC的背景色
	memdc.FillSolidRect(0, 0, 1000, 1000, RGB(240, 240, 240));

	// 画曲线图
	memdc.MoveTo(x0, y0); // 从原点开始
	// 画每一个点的连线
	int i;
	for (i = 0; i < 500; i++)
		memdc.LineTo(x0 + i, y0 - data1[i]);

	// 把内存DC复制到客户区DC
	dc.BitBlt(0, 30, 1000, 1000, &memdc, 0, 0, SRCCOPY);
## 文件操作
### 准备工作
![](%E4%BB%A3%E7%A0%81%E6%B1%87%E6%80%BB_md_files/71add880-b5b5-11ed-8327-4193e6e43d4a_20230226171043.jpeg?v=1&type=image&token=V1:fzeqRixAhhLpV1WbIE18M5aHN-1VTiVhK8m6PMk0CL4)
### 文件对话框操作

	CFileDialog fileDlg(true); // 读文件对话框

	fileDlg.DoModal(); // 打开对话框

	CString filename = fileDlg.GetPathName(); // 获取文件名

	fp1 = fopen(CStringA(filename), "r"); // 打开文本文件读
### 打开文件
	FILE *fp1; // 定义文件指针

	fp1 = fopen("文本文件.txt", "r"); // 打开文本文件用于读

	if (fp1 == NULL) // 文件打开错误
	{
		MessageBox(L"文件打开错误！", 0, 0);
		return;
	}

![](%E4%BB%A3%E7%A0%81%E6%B1%87%E6%80%BB_md_files/d893f480-b5b0-11ed-8327-4193e6e43d4a_20230226163748.jpeg?v=1&type=image&token=V1:Hxro4qNYhbl4ImvjH22QmdZRD7FwmL26_kwnkfbqjGY)
### 读取文件
经常读到数组里面，关注数值分隔符！
文本文件读取：

	char data1[10000]; // char型
	int data2[10000]; // 整型 
	float data3[10000]; // 浮点型
	int i = 0; // 数组下标

	// 以格式化方式读入多行数值，数值分隔符为逗号
	// 行分隔符为\n 
	while (!feof(fp1)) // 未到文件尾
	{
		fscanf(fp1, "%d,%d,%f\n", &data1[i], &data2[i], &data3[i]); // 读一行数据
		i++;
	}

	fclose(fp1); // 关闭文件
### 写入文件
二进制文件写入：

	FILE *fp2; // 定义文件指针

	fp2 = fopen("二进制文件.dat", "wb"); // 打开二进制文件用于写
	if (fp2 == NULL) // 文件打开错误
	{
		MessageBox(L"文件打开错误！",0,0);
		return;
	}

	for (int i = 0; i <= 9; i++) 
	{
	fwrite(&data1[i], sizeof(char), 1, fp2); // 写一个整型
	fwrite(&data2[i], sizeof(int), 1, fp2); // 写一个整型
	fwrite(&data3[i], sizeof(float), 1, fp2); // 写一个单精度浮点型

	}

	fclose(fp2); // 关闭文件

文本文件读写：
- 格式化写

`fprintf(fp, “%d,%f,%c,%s”, data1, data2, data3, data4);`

-  格式化读

`fscanf(fp, “%d,%f,%c,%s”, &data1, &data2, &data3, &data4);`
二进制文件读写：

- 格式化写：

`fwrite(&data1, sizeof(int), 1, fp);`

- 格式化读

`fread(&data1, sizeof(int), 1, fp);`

### 二进制、文本文件转化

	FILE *fp3; // 定义文件指针

	fp3 = fopen("二进制文件.dat", "rb"); // 打开二进制文件用于读
	if (fp3 == NULL) // 文件打开错误
	{
		MessageBox(L"文件打开错误！",0,0);
		return;
	}

	char data4[10000]; // 整型
	int data5[10000]; // 整型 
	float data6[10000]; // 浮点型
	int i = 0; // 数组下标

	
	for (int i = 0; i <= 9; i++) 
	{

	fread(&data4[i], sizeof(char), 1, fp3); // 写一个char型
	fread(&data5[i], sizeof(int), 1, fp3); // 写一个整型
	fread(&data6[i], sizeof(float), 1, fp3); // 写一个单精度浮点型

	}

	fclose(fp3); // 关闭文件

	
	FILE *fp4; // 定义文件指针

	fp4 = fopen("复制文件.txt", "w"); // 打开文本文件用于写
	if (fp4 == NULL) // 文件打开错误
	{
		MessageBox(L"文件打开错误！",0,0);
		return;
	}
	// 以格式化方式将数值写入文本文件，分隔符为逗号
	// 注意字符型变量 c 分别以 %c 和 %d 的格式写入 
	for (int i = 0; i <= 9; i++) 
	{
		fprintf(fp4, "%d,%d,%0.1f\n", data4[i],data5[i],data6[i]);
	}

	fclose(fp4); // 关闭文件
## 随机数生成器
![](%E4%BB%A3%E7%A0%81%E6%B1%87%E6%80%BB_md_files/6467ac10-b5b4-11ed-8327-4193e6e43d4a_20230226170311.jpeg?v=1&type=image&token=V1:CzZk47KTwbb2oPI0UnVnHJaAXI8ES8RwSHSKNQNwUns)
## 网络编程
**须选取Windows套接字**

	UpdateData(true);

	//定义CSocket对象
	CSocket socket;
	//创建套接字
	socket.Create();

	//连接服务器,地址:127.0.0.1, 端口8000
	if (!socket.Connect(L"127.0.0.1", 8000))
	{
		MessageBox(L"与服务器链接失败!", 0, 0);
		return;
	}

	//向服务器发送字符串
	socket.Send(CStringA(sendStr), 256);

	// 接收服务器的回复
	char buf[256] = { 0 };
	socket.Receive(buf, 255);//同步阻塞式等待接收
	recvStr = buf;// 回复的字符串
		//断开与服务器的连接
	socket.Close();

	UpdateData(false);

	
**接受服务器传达的信息后，务必记得断开与服务器的连接**
收到字符串后，按照如下方式对字符串进行处理：

- 用Find()函数从字符串中找到子串的位置

- i = str.Find(substr, p);

- 子串为字符串时，须加L

- 从字符串 str 的第 p 个字符开始搜索字符串 substr

- 搜索到的第一个 substr 的起始位置保存在 i 中

- **如果 str 中不包含 substr 则 i=-1**

- 一个英文字母占1个字符位置，一个汉字占2个字符

位置
- 结果返回该子串首字母所在的位置

## Mid函数：
从任意位置开始截取给定长度的字符串
`Mid(start,lenth)`
## 字符串类型转化
- CString 转 int
```
int n;
n = atoi(CStringA(str));
```

- CString 转 float
```
float x;
x = atof(CStringA(str));
```
## 课件内容索引：
常见错误：
判断语句用 ==
课件11中的条件语句错误
if (t3 == 0 || t3 == 7 || t3 == 9 || t3 == 12）

课件3：
if,else if,else 之间的辨析
UpdateData
comboBox：sort 自动排序
                     ”数据“ 用;隔开

课件4：
函数的 声明 定义 调用
  变量的 定义 初始化 使用
CString类变量 字符串 可以中英文混杂 不区分大小写

课件5：
结构体变量 struct
两种初始化方式
常见RGB组合
黄255，255，0；紫/粉255，0，255；淡蓝/青0，255，255；白255，255，255；黑0，0，0
画点：SetPixel(x,y,RGB(r,g,b));
画线：MoveTo(x,y); LineTo(x,y);
画矩形：Rectangle(x1,y1,x2,y2);
画笔类对象  6种线型（包括无边框）
画刷类对象  
画矩形 画椭圆
边框颜色由画笔决定

课件6：
CPoint类对象
文本输出
随机数生成
清空客户区
鼠标键盘消息

课件7：
随机数生成
鼠标键盘消息
设定前景色的混合模式
图片控件

课件8：
图片控件和句柄
控件绑定变量
CString的使用和相关函数

课件9：
显示图片 BitBlt函数
内存DC
地雷

课件10：
计时器

课件11：
动态曲线图
控件大小和位置 uFlags
填充矩形
内存DC

课件12：
文件的读写
字符和字符串的辨析
字符串相关函数
4996

课件13：
变量转换
文件对话框

课件14：
网络通话


练习2：冰雹+WInRabbit

练习3：冰雹2.0+计算器

练习4：冰雹3.0（函数化）也与计算器相关
在 CollatzDlg.h 文件中添加函数的声明
afx_msg void addNumber(int num);
在 CollatzDlg.cpp 文件中添加函数的定义
void CCollatzDlg::addNumber(int num)
{
在这里编写函数的内容
}
隐藏按钮：改属性
/:整除，%:取余

           DataEngine
下拉列表框的Type=下拉列表
和消息类型=CBN_SELCHANGE

练习5：draw+DataEngine2.0（结构体数组化＋柱折图）

练习6：clickDraw（调色板与输出字符）+DataEngine3.0（判断点击位置）

练习7：ddraw(鼠标画线+橡皮擦效果）+lightControl

练习8：lightControl2.0(句柄+隐藏图片控件）+DataEngine4.0（标题文字OnPaint函数else处）

练习9：lightControl3.0（函数化+状态）+地雷（网格线+图片缓存CDC句柄）

练习10：lightControl4.0（计时器，sos）+DataEngine5.0（动画）

练习11：动态曲线（向前平移数据，两种方法，坐标轴）

练习12：文件（4996+文件的打开与读写+变量的转换）+DataEngine6.0（下拉列表框添加内容变量：
初始化处for (int i = 0; i < count; i++)
comboName.AddString(data[i].name);
）

练习13：疫情数据+DataEngine7.0（读入数据）

练习14：网络（套接字+变量+分解）

综合项目：（单选框）
