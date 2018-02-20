' LoopThroughWorksheets function loops through all the worksheets in the active workbook
' It calls 'AnalyzeStockData' function to analyze stock data in all the worksheets
Sub LoopThroughWorksheets()

    Dim WorkSheet_Count As Integer
    Dim I As Integer

    ' Number of worksheets in the project workbook
    WorkSheet_Count = ActiveWorkbook.Worksheets.Count

    ' Iterate through the worksheets
    For I = 1 To WorkSheet_Count

       ' Activate worksheet and Analyze stock data
       ActiveWorkbook.Worksheets(I).Activate
       Call AnalyzeStockData

    Next I
End Sub


' AnalyzeStockData analyzes the stock data in active excel worksheet
' Calculates total stock volume of each ticker given in worksheet
' Calculates yearly change of the stock and percentage of change in volume
' Calculates greatest increase, greatest decrease and greatest total volume
Sub AnalyzeStockData()

    Dim I As Long
    Dim J As Long
    Dim Total_Records As Long
    Dim Ticker_Counter As Integer
    Dim StockPrice_Open As Double
    Dim StockPrice_Close As Double
    Dim Stock_Volume As Double
    Dim Yearly_Change As Double
    Dim Percent_Change As Double
    Dim Greatest_Increase As Double
    Dim Greatest_Decrease As Double
    Dim Greatest_Total_Volume As Double
 
    Range("I1").Value = "Ticker"
    Range("J1").Value = "Yearly Change"
    Range("K1").Value = "Percent Change"
    Range("L1").Value = "Total Stock Volume"
    
    Total_Records = Cells(Rows.Count, 1).End(xlUp).Row
    StockPrice_Open = Cells(2, 3).Value

    J = 2
    Ticker_Counter = 1
    For I = 2 To Total_Records
        StockPrice_Open = Cells(J, 3).Value
            
        'Calculate total volume stock for each ticker
        If Cells(I, 1).Value = Cells(I + 1, 1).Value Then
            Stock_Volume = Stock_Volume + Cells(I, 7).Value
        Else
            Stock_Volume = Stock_Volume + Cells(I, 7).Value
            StockPrice_Close = Cells(I, 6).Value
            Yearly_Change = StockPrice_Close - StockPrice_Open
            If StockPrice_Open = 0# Then
                Percent_Change = 0#
            Else
                Percent_Change = Yearly_Change / StockPrice_Open
            End If
            Cells(Ticker_Counter + 1, 9).Value = Cells(I, 1).Value
            Cells(Ticker_Counter + 1, 10).Value = Yearly_Change
            If Yearly_Change > 0 Then
                Cells(Ticker_Counter + 1, 10).Interior.ColorIndex = 10
            ElseIf Yearly_Change < 0 Then
                Cells(Ticker_Counter + 1, 10).Interior.ColorIndex = 3
            End If
            Cells(Ticker_Counter + 1, 11).Value = Percent_Change
            Cells(Ticker_Counter + 1, 11).NumberFormat = "0.00%"
            Cells(Ticker_Counter + 1, 12).Value = Stock_Volume
            Ticker_Counter = Ticker_Counter + 1
          
        
            Stock_Volume = 0
            J = I + 1
        End If
    Next I
    
     
        'Calculate greatest increase
        Greatest_Increase = Cells(2, 11).Value
        For I = 3 To Ticker_Counter
    
            If Cells(I, 11).Value > Greatest_Increase Then
                Greatest_Increase = Cells(I, 11).Value
                ticker = Cells(I, 9).Value
            End If
        Next I
        
        Range("P1").Value = "Ticker"
        Range("Q1").Value = "Value"
        Range("O2").Value = "Greatest % Increase"
        Range("P2").Value = ticker
        Range("Q2").Value = Greatest_Increase
        Range("Q2").NumberFormat = "0.00%"
        
        'Calculate greatest decrease
        Greatest_Decrease = Cells(2, 11).Value
        For I = 3 To Ticker_Counter
            If Cells(I, 11).Value < Greatest_Decrease Then
                Greatest_Decrease = Cells(I, 11).Value
                ticker = Cells(I, 9).Value
            End If
        Next I
      
        
        Range("O3").Value = "Greatest % Decrease"
        Range("P3").Value = ticker
        Range("Q3").Value = Greatest_Decrease
        Range("Q3").NumberFormat = "0.00%"
        
        'Calculate greastest total volume of stock
        Greatest_Total_Volume = Cells(2, 12).Value
        For I = 3 To Ticker_Counter
            If Cells(I, 12).Value > Greatest_Total_Volume Then
                Greatest_Total_Volume = Cells(I, 12).Value
                ticker = Cells(I, 9).Value
            End If
        Next I
        
        Range("P4").Value = ticker
        Range("O4").Value = "Greatest Total Volume"
        Range("Q4").Value = Greatest_Total_Volume
End Sub
