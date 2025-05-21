from django.http import JsonResponse
from .backtest import run_backtest
from django.shortcuts import render

def backtest_view(request):
    try:
        df1, df2, df3, df4 = run_backtest()

        return JsonResponse({
            "status": "ok",
            "summary": df1.to_dict(orient="records"),
            "pivot": df2.to_dict(orient="records"),
            "correlation": df3.to_dict(),
            "logprice": df4.to_dict(orient="records")
        }, json_dumps_params={"ensure_ascii": False})
    
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)

def backtest_page(request):
    return render(request, "trading/backtest.html")

def auto_trading_view(request):
    # TODO: 실시간 자동매매 로직 연결
    return JsonResponse({"mode": "auto-trading", "status": "started"})
