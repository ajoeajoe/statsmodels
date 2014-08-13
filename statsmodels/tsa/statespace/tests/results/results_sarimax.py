"""
Results for SARIMAX tests

Results from Stata using script `test_sarimax_stata.do`.
See also Stata time series documentation.

Data from:

http://www.stata-press.com/data/r12/wpi1
http://www.stata-press.com/data/r12/air2
http://www.stata-press.com/data/r12/friedman2

Author: Chad Fulton
License: Simplified-BSD
"""

wpi1_data = [
    30.70000076,   30.79999924,   30.70000076,   30.70000076,
    30.79999924,   30.5       ,   30.5       ,   30.60000038,
    30.70000076,   30.60000038,   30.70000076,   30.70000076,
    30.60000038,   30.5       ,   30.60000038,   30.70000076,
    30.70000076,   30.60000038,   30.70000076,   30.70000076,
    30.89999962,   31.20000076,   31.39999962,   31.60000038,
    32.09999847,   32.20000076,   32.59999847,   32.40000153,
    32.29999924,   32.29999924,   32.40000153,   32.5       ,
    32.90000153,   33.09999847,   33.29999924,   33.40000153,
    33.90000153,   34.40000153,   34.70000076,   35.        ,
    35.5       ,   35.70000076,   35.90000153,   35.90000153,
    36.5       ,   36.90000153,   37.20000076,   37.20000076,
    37.90000153,   38.29999924,   38.79999924,   39.20000076,
    41.09999847,   43.09999847,   44.90000153,   45.29999924,
    48.29999924,   50.        ,   53.59999847,   55.40000153,
    55.40000153,   56.        ,   57.20000076,   57.79999924,
    58.09999847,   59.        ,   59.70000076,   60.20000076,
    61.59999847,   63.        ,   63.09999847,   63.90000153,
    65.40000153,   67.40000153,   68.40000153,   70.        ,
    72.5       ,   75.09999847,   77.40000153,   80.19999695,
    83.90000153,   85.59999847,   88.40000153,   90.40000153,
    93.09999847,   95.19999695,   95.90000153,   95.80000305,
    96.59999847,   96.69999695,   97.09999847,   97.19999695,
    97.30000305,   97.59999847,   98.59999847,   99.09999847,
    100.19999695,  100.80000305,  100.59999847,  100.30000305,
    100.09999847,  100.19999695,   99.5       ,  100.09999847,
    98.59999847,   96.80000305,   96.30000305,   96.69999695,
    97.80000305,   99.40000153,  100.5       ,  101.        ,
    101.59999847,  103.19999695,  104.69999695,  105.19999695,
    107.5       ,  109.40000153,  109.        ,  109.40000153,
    111.        ,  110.80000305,  112.80000305,  116.19999695
]
wpi1_stationary = {
    'data': wpi1_data,
    'params_ar': [.8742288],
    'se_ar': [.0545435],
    'params_ma': [-.4120458],
    'se_ma': [.1000284],
    'params_mean': [.7498197],
    'se_mean': [.3340968],
    'params_variance': [.7250436**2],
    'se_variance': [.0368065],
    'loglike': -135.35131,
    'aic': 278.7026,
    'bic': 289.9514,
}

wpi1_diffuse = {
    'data': wpi1_data,
    'initial_variance': 1e9,
    'params_ar': [.864419],
    'se_ar': [.0563637],
    'params_ma': [-.3960891],
    'se_ma': [.1018369],
    'params_mean': [.8412064],
    'se_mean': [.3159328],
    'params_variance': [.7282775**2],
    'se_variance': [.0373227],
    'loglike': -154.29177,
    'aic': 316.5835,
    'bic': 327.8323,
}

wpi1_seasonal = {
    'data': wpi1_data,
    'params_ar': [.7806991],
    'se_ar': [.0944946],
    'params_ma': [-.3990039, .3090813],
    'se_ma': [.1258753, .1200945],
    'params_mean': [.0110493],
    'se_mean': [.0048349],
    'params_variance': [.0104394**2],
    'se_variance': [.0004702],
    'loglike': 386.03357,
    'aic': -762.0671,
    'bic': -748.0062,
}

air2_data = [
    112, 118, 132, 129, 121, 135, 148, 148, 136, 119, 104, 118, 115,
    126, 141, 135, 125, 149, 170, 170, 158, 133, 114, 140, 145, 150,
    178, 163, 172, 178, 199, 199, 184, 162, 146, 166, 171, 180, 193,
    181, 183, 218, 230, 242, 209, 191, 172, 194, 196, 196, 236, 235,
    229, 243, 264, 272, 237, 211, 180, 201, 204, 188, 235, 227, 234,
    264, 302, 293, 259, 229, 203, 229, 242, 233, 267, 269, 270, 315,
    364, 347, 312, 274, 237, 278, 284, 277, 317, 313, 318, 374, 413,
    405, 355, 306, 271, 306, 315, 301, 356, 348, 355, 422, 465, 467,
    404, 347, 305, 336, 340, 318, 362, 348, 363, 435, 491, 505, 404,
    359, 310, 337, 360, 342, 406, 396, 420, 472, 548, 559, 463, 407,
    362, 405, 417, 391, 419, 461, 472, 535, 622, 606, 508, 461, 390, 432
]
air2_stationary = {
    'data': air2_data,
    'params_ma': [-.4018324],
    'se_ma': [.0730307],
    'params_seasonal_ma': [-.5569342],
    'se_seasonal_ma': [.0963129],
    'params_variance': [.0367167**2],
    'se_variance': [.0020132],
    'loglike': 244.69651,
    'aic': -483.393,
    'bic': -474.7674,
}

friedman2_data = {'consump': [
         310.3999939 ,   316.3999939 ,   321.70001221,   323.79998779,
         327.29998779,   333.20001221,   333.1000061 ,   335.        ,
         335.70001221,   340.6000061 ,   343.5       ,   350.70001221,
         355.29998779,   361.29998779,   365.3999939 ,   371.70001221,
         375.1000061 ,   379.3999939 ,   386.3999939 ,   391.1000061 ,
         400.5       ,   408.29998779,   417.1000061 ,   419.79998779,
         430.6000061 ,   437.79998779,   447.20001221,   461.5       ,
         472.        ,   477.1000061 ,   486.3999939 ,   492.        ,
         496.79998779,   506.20001221,   513.70001221,   521.20001221,
         539.5       ,   553.20001221,   569.09997559,   577.5       ,
         588.79998779,   599.40002441,   609.20001221,   621.09997559,
         632.40002441,   642.70001221,   655.20001221,   662.09997559,
         681.59997559,   695.79998779,   708.20001221,   724.5       ,
         741.90002441,   759.90002441,   778.09997559,   802.90002441,
         827.20001221,   842.09997559,   860.79998779,   876.09997559,
         894.40002441,   922.40002441,   950.09997559,   957.79998779,
         982.70001221,  1012.40002441,  1046.30004883,  1075.09997559,
        1110.19995117,  1130.19995117,  1159.80004883,  1195.        ,
        1230.69995117,  1259.09997559,  1290.30004883,  1328.09997559,
        1358.30004883,  1417.40002441,  1450.59997559,  1488.69995117,
        1529.30004883,  1563.90002441,  1617.40002441,  1663.5       ,
        1713.09997559,  1716.90002441,  1774.90002441,  1836.80004883,
        1890.30004883,  1923.5       ,  1967.40002441,  1983.90002441
], 'm2': [
         289.1499939 ,   294.04998779,   296.73001099,   297.79998779,
         299.3500061 ,   302.32998657,   308.45001221,   312.36999512,
         318.29000854,   324.29000854,   329.54000854,   335.5       ,
         343.1000061 ,   349.25      ,   354.86999512,   362.72000122,
         370.66000366,   378.42001343,   386.01998901,   393.23999023,
         399.76000977,   407.07998657,   416.88000488,   424.73999023,
         433.22000122,   440.1000061 ,   449.48999023,   459.17001343,
         467.22000122,   471.1499939 ,   475.42999268,   480.16000366,
         489.67001343,   502.        ,   514.65997314,   524.77001953,
         533.16998291,   542.60998535,   553.55999756,   566.84997559,
         574.35998535,   578.4699707 ,   582.05999756,   587.90002441,
         587.26000977,   595.15997314,   611.20001221,   626.54998779,
         649.90002441,   672.96002197,   692.4699707 ,   710.26000977,
         733.5       ,   749.66998291,   778.35998535,   802.2800293 ,
         815.30999756,   833.22998047,   839.27001953,   855.52001953,
         870.11999512,   877.82000732,   888.15997314,   902.41998291,
         925.55999756,   963.30999756,   991.7199707 ,  1016.98999023,
        1050.0300293 ,  1077.70996094,  1111.31005859,  1152.7800293 ,
        1188.80004883,  1217.67004395,  1246.90002441,  1271.4699707 ,
        1292.86999512,  1318.09997559,  1346.81005859,  1368.01000977,
        1388.9699707 ,  1423.2199707 ,  1456.85998535,  1475.75      ,
        1501.81994629,  1529.52001953,  1576.0300293 ,  1601.09997559,
        1638.        ,  1670.55004883,  1708.38000488,  1756.18994141
]}

friedman2_mle = {
    'data': friedman2_data,
    'params_exog': [-36.09872, 1.122029],
    'se_exog': [56.56703, .0363563],
    'params_ar': [.9348486],
    'se_ar': [.0411323],
    'params_ma': [.3090592],
    'se_ma': [.0885883],
    'params_variance': [9.655308**2],
    'se_variance': [.5635157],
    'loglike': -340.50774,
    'aic': 691.0155,
    'bic': 703.6244,
}

# 1959q1 - 1981q4
friedman2_prediction = [
    300.7722, 314.699, 318.3328, 322.1395, 324.1479, 329.3138, 338.3326,
    334.2127, 340.1221, 340.1285, 345.7686, 348.9585, 358.8476, 360.8798,
    367.4761, 373.4112, 380.132, 383.0179, 388.0034, 395.276, 398.8789,
    410.393, 419.7131, 426.5234, 429.3965, 440.4875, 449.2072, 459.1391,
    472.4367, 477.6227, 482.9371, 493.2135, 502.3943, 509.5284, 520.3149,
    524.9484, 531.8344, 553.2029, 565.8674, 584.5371, 584.7531, 595.1661,
    604.5025, 616.0223, 620.5868, 641.1515, 656.7986, 668.2184, 683.2755,
    704.2855, 714.1062, 726.3972, 749.7296, 758.9711, 792.2435, 802.7343,
    820.1996, 850.1489, 849.0018, 882.2756, 891.0745, 904.4603, 936.7991,
    965.2041, 977.2533, 1020.77, 1038.109, 1072.798, 1107.716, 1137.204,
    1161.788, 1201.592, 1230.821, 1261.099, 1289.544, 1316.565, 1352.555,
    1384.148, 1450.45, 1466.267, 1508.321, 1560.003, 1589.353, 1631.959,
    1683.234, 1731.301, 1745.414, 1792.131, 1866.122, 1907.568, 1944.034,
    1999.784
]

# 1959q1 - 1981q4
# Dynamic after 1978q1
friedman2_dynamic_prediction = [
    300.7722, 314.699, 318.3328, 322.1395, 324.1479, 329.3138, 338.3326,
    334.2127, 340.1221, 340.1285, 345.7686, 348.9585, 358.8476, 360.8798,
    367.4761, 373.4112, 380.132, 383.0179, 388.0034, 395.276, 398.8789,
    410.393, 419.7131, 426.5234, 429.3965, 440.4875, 449.2072, 459.1391,
    472.4367, 477.6227, 482.9371, 493.2135, 502.3943, 509.5284, 520.3149,
    524.9484, 531.8344, 553.2029, 565.8674, 584.5371, 584.7531, 595.1661,
    604.5025, 616.0223, 620.5868, 641.1515, 656.7986, 668.2184, 683.2755,
    704.2855, 714.1062, 726.3972, 749.7296, 758.9711, 792.2435, 802.7343,
    820.1996, 850.1489, 849.0018, 882.2756, 891.0745, 904.4603, 936.7991,
    965.2041, 977.2533, 1020.77, 1038.109, 1072.798, 1107.716, 1137.204,
    1161.788, 1201.592, 1230.821, 1261.099, 1289.544, 1316.565, 1352.555,
    1377.515, 1406.237, 1427.295, 1448.221, 1483.042, 1517.318, 1536.364,
    1562.931, 1591.249, 1639.144, 1664.832, 1702.839, 1736.367, 1775.407,
    1824.832
]

# 1959q1 - 1981q4
# Forecasts after 1978q1
friedman2_forecast = [
    300.7722, 314.699, 318.3328, 322.1395, 324.1479, 329.3138, 338.3326,
    334.2127, 340.1221, 340.1285, 345.7686, 348.9585, 358.8476, 360.8798,
    367.4761, 373.4112, 380.132, 383.0179, 388.0034, 395.276, 398.8789,
    410.393, 419.7131, 426.5234, 429.3965, 440.4875, 449.2072, 459.1391,
    472.4367, 477.6227, 482.9371, 493.2135, 502.3943, 509.5284, 520.3149,
    524.9484, 531.8344, 553.2029, 565.8674, 584.5371, 584.7531, 595.1661,
    604.5025, 616.0223, 620.5868, 641.1515, 656.7986, 668.2184, 683.2755,
    704.2855, 714.1062, 726.3972, 749.7296, 758.9711, 792.2435, 802.7343,
    820.1996, 850.1489, 849.0018, 882.2756, 891.0745, 904.4603, 936.7991,
    965.2041, 977.2533, 1020.77, 1038.109, 1072.798, 1107.716, 1137.204,
    1161.788, 1201.592, 1230.821, 1261.099, 1289.544, 1316.565, 1352.555,
    1384.148, 1412.057, 1432.403, 1452.703, 1486.975, 1520.77, 1539.393,
    1565.588, 1593.582, 1641.19, 1666.628, 1704.415, 1737.75, 1776.62,
    1825.897
]

# 1959q1 - 1981q4
# Forecasts after 1978q1 (and dynamic)
# This (the dynamic part) is not necessarily a sensible thing to do, but this
# is just a unit test
friedman2_dynamic_forecast = [
    300.7722, 314.699, 318.3328, 322.1395, 324.1479, 329.3138, 338.3326,
    334.2127, 340.1221, 340.1285, 345.7686, 348.9585, 358.8476, 360.8798,
    367.4761, 373.4112, 380.132, 383.0179, 388.0034, 395.276, 398.8789,
    410.393, 419.7131, 426.5234, 429.3965, 440.4875, 449.2072, 459.1391,
    472.4367, 477.6227, 482.9371, 493.2135, 502.3943, 509.5284, 520.3149,
    524.9484, 531.8344, 553.2029, 565.8674, 584.5371, 584.7531, 595.1661,
    604.5025, 616.0223, 620.5868, 641.1515, 656.7986, 668.2184, 683.2755,
    704.2855, 714.1062, 726.3972, 749.7296, 758.9711, 792.2435, 802.7343,
    820.1996, 850.1489, 849.0018, 882.2756, 891.0745, 904.4603, 936.7991,
    965.2041, 977.2533, 1020.77, 1038.109, 1072.798, 1107.716, 1137.204,
    1161.788, 1201.592, 1230.821, 1261.099, 1289.544, 1316.565, 1352.555,
    1377.515, 1406.237, 1427.295, 1448.221, 1483.042, 1517.318, 1536.364,
    1562.931, 1591.249, 1639.144, 1664.832, 1702.839, 1736.367, 1775.407,
    1824.832
]

friedman2_predict = {
    'data': friedman2_data,
    'predict': friedman2_prediction,
    'dynamic_predict': friedman2_dynamic_prediction,
    'forecast': friedman2_forecast,
    'dynamic_forecast': friedman2_dynamic_forecast,
    'params_exog': [.66189, 1.037905],
    'params_ar': [.8775207],
    'params_ma': [.2770867],
    'params_variance': [5.630046**2],
    'loglike': -243.31642,
    'aic': 496.6328,
    'bic': 508.3519,
}
