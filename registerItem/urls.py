from django.urls import path
from . import views
# from registerItem.views import stockSearchView

urlpatterns = [

    path('recorditem/<int:pk>/', views.recordItem, name='recorditem'),
# ==================sector register item ============
    path('recorditem-sector/<int:pk>/', views.sectorRecordItem, name='recorditem_sector'),

    path('all_item/', views.allItem, name='all_item'),

    path('updateitem/<str:pk>/', views.updateItem, name='updateitem'),
    path('deleteitem/<str:pk>/', views.deleteItem, name='deleteitem'),

    path('recordstock/', views.recordStock, name='recordstock'),
    path('updatestock/<str:pk>/', views.updateStock, name='updatestock'),
    path('deletestock/<str:pk>/', views.deleteStock, name='deletestock'),
    path('allstock/', views.allStock, name='allstock'),
   ## ============JAVASCRIPT SEARCH=================
    # path('search/', stockSearchView.as_view(), name='search'),


    path('available_stock/', views.availableDevice, name='available_stock'),

# =================== SECTOR RECORD DEVICE ======================================
    path('recordstock-sector/', views.sectorRecordStock, name='recordstock_sector'),
    path('allstock-sector/', views.sectorStockList, name='allstock_sector'),


    path('sector-laptop', views.sectorLaptop, name='sector_laptop'),
    path('sector_update_lap/<int:pk>', views.sectorLaptopUpdate, name='sector_update_lap'),

    path('sector_desktop', views.sectorDesktop, name='sector_desktop'),
    path('sector_update_desktop/<int:pk>', views.sectorDesktopUpdate, name='sector_update_desktop'),

    path('sector_printer', views.sectorPrinter, name='sector_printer'),
    path('sector_update_printer/<int:pk>', views.sectorPrinterUpdate, name='sector_update_printer'),

    path('sector_router', views.sectorRouter, name='sector_router'),
    path('sector_update_router/<int:pk>', views.sectorRouterUpdate, name='sector_update_router'),

    path('sector_scanner', views.sectorScanner, name='sector_scanner'),
    path('sector_update_scanner/<int:pk>', views.sectorScannerUpdate, name='sector_update_scanner'),

    path('sector_television', views.sectorTelevision, name='sector_television'),
    path('sector_update_television/<int:pk>', views.sectorTelevisionUpdate, name='sector_update_television'),

    path('sector_decoder', views.sectorDecoder, name='sector_decoder'),
    path('sector_update_decoder/<int:pk>', views.sectorDecoderUpdate, name='sector_update_decoder'),

    path('gishamvu-report/', views.gishamvuReport, name='gishamvu_report'),
    path('huye-report/', views.huyeReport, name='huye_report'),
    path('karama-report/', views.karamaReport, name='karama_report'),
    path('kigoma-report/', views.kigomaReport, name='kigoma_report'),
    path('kinazi-report/', views.kinaziReport, name='kinazi_report'),
    path('maraba-report/', views.marabaReport, name='maraba_report'),
    path('mbazi-report/', views.mbaziReport, name='mbazi_report'),
    path('mukura-report/', views.mukuraReport, name='mukura_report'),
    path('ngoma-report/', views.ngomaReport, name='ngoma_report'),
    path('ruhashya-report/', views.ruhashyaReport, name='ruhashya_report'),
    path('rusatira-report/', views.rusatiraReport, name='rusatira_report'),
    path('rwaniro-report/', views.rwaniroReport, name='rwaniro_report'),
    path('simbi-report/', views.simbiReport, name='simbi_report'),
    path('tumba-report/', views.tumbaReport, name='tumba_report'),
    path('huyedistrict-report/', views.districtOfficeReport, name='huyedistrict_report'),

# ==============FULL REPORT ALL GIVEN ITEMS ====================
    path('full-given-report/', views.fullReport, name='full_given_report'),




    path('sector_report/', views.tableReport, name='sector_report'),
# ====================== SEARCHING ====================
    path('stock-generate/', views.allStockSearch, name='stock_generate'),
    # =======================generate report ================
    path('karama-generate/', views.karamaReportGenerate, name='karama_generate'),
    path('huye-generate/', views.huyeReportGenerate, name='huye_generate'),
    path('huyedistrict-generate/', views.districtReportGenerate, name='huyedistrict_generate'),
    path('kigoma-generate/', views.kigomaReportGenerate, name='kigoma_generate'),
    path('kinazi-generate/', views.kinaziReportGenerate, name='kinazi_generate'),
    path('maraba-generate/', views.marabaReportGenerate, name='maraba_generate'),
    path('mbazi-generate/', views.mbaziReportGenerate, name='mbazi_generate'),
    path('mukura-generate/', views.mukuraReportGenerate, name='mukura_generate'),
    path('ngoma-generate/', views.ngomaReportGenerate, name='ngoma_generate'),
    path('ruhashya-generate/', views.ruhashyaReportGenerate, name='ruhashya_generate'),
    path('rusatira-generate/', views.rusatiraReportGenerate, name='rusatira_generate'),
    path('rwaniro-generate/', views.rwaniroReportGenerate, name='rwaniro_generate'),
    path('simbi-generate/', views.simbiReportGenerate, name='simbi_generate'),
    path('tumba-generate/', views.tumbaReportGenerate, name='tumba_generate'),
    path('gishamvu-generate/', views.gishamvuReportGenerate, name='gishamvu_generate'),
    path('full-report-generate/', views.fullReportGenerate, name='full_report_generate'),


]
