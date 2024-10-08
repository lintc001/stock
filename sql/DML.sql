USE stock;

INSERT INTO market (id,name) VALUE ('sii','上市'), ('otc','上櫃');


/*-----------------------------------------------------------*/
INSERT INTO industry (id, market_id, name) VALUE ('01','sii',	'水泥工業'),
                                               ('02','sii',	'食品工業'),
                                               ('03','sii',	'塑膠工業'),
                                               ('04','sii',	'紡織纖維'),
                                               ('05','sii',	'電機機械'),
                                               ('06','sii',	'電器電纜'),
                                               ('07','sii',	'化學生技醫療'),
                                               ('08','sii',	'玻璃陶瓷'),
                                               ('09','sii',	'造紙工業'),
                                               ('10','sii',	'鋼鐵工業'),
                                               ('11','sii',	'橡膠工業'),
                                               ('12','sii',	'汽車工業'),
                                               ('13','sii',	'電子工業'),
                                               ('14','sii',	'建材營造'),
                                               ('15','sii',	'航運業'),
                                               ('16','sii',	'觀光餐旅業'),
                                               ('17','sii',	'金融保險業'),
                                               ('18','sii',	'貿易百貨'),
                                               ('19','sii',	'綜合企業'),
                                               ('20','sii',	'其他'),
                                               ('21','sii',	'化學工業'),
                                               ('22','sii',	'生技醫療業'),
                                               ('23','sii',	'油電燃氣業'),
                                               ('24','sii',	'半導體業'),
                                               ('25','sii',	'電腦及週邊設備業'),
                                               ('26','sii',	'光電業'),
                                               ('27','sii',	'通信網路業'),
                                               ('28','sii',	'電子零組件業'),
                                               ('29','sii',	'電子通路業'),
                                               ('30','sii',	'資訊服務業'),
                                               ('31','sii',	'其他電子業'),
                                               ('35','sii',	'綠能環保業'),
                                               ('36','sii',	'數位雲端業'),
                                               ('37','sii',	'運動休閒業'),
                                               ('38','sii',	'居家生活業'),
                                               ('91','sii',	'存託憑證');

INSERT INTO industry (id, market_id, name) VALUE ('02', 'otc', '食品工業'),
                                                 ('03', 'otc', '塑膠工業'),
                                                 ('04', 'otc', '紡織纖維'),
                                                 ('05', 'otc', '電機機械'),
                                                 ('06', 'otc', '電器電纜'),
                                                 ('07', 'otc', '化學生技醫療'),
                                                 ('08', 'otc', '玻璃陶瓷'),
                                                 ('10', 'otc', '鋼鐵工業'),
                                                 ('11', 'otc', '橡膠工業'),
                                                 ('13', 'otc', '電子工業'),
                                                 ('14', 'otc', '建材營造'),
                                                 ('15', 'otc', '航運業'),
                                                 ('16', 'otc', '觀光餐旅業'),
                                                 ('17', 'otc', '金融業'),
                                                 ('20', 'otc', '其他'),
                                                 ('21', 'otc', '化學工業'),
                                                 ('22', 'otc', '生技醫療業'),
                                                 ('23', 'otc', '油電燃氣業'),
                                                 ('24', 'otc', '半導體業'),
                                                 ('25', 'otc', '電腦及週邊設備業'),
                                                 ('26', 'otc', '光電業'),
                                                 ('27', 'otc', '通信網路業'),
                                                 ('28', 'otc', '電子零組件業'),
                                                 ('29', 'otc', '電子通路業'),
                                                 ('30', 'otc', '資訊服務業'),
                                                 ('31', 'otc', '其他電子業'),
                                                 ('32', 'otc', '文化創意業'),
                                                 ('33', 'otc', '農業科技'),
                                                 ('35', 'otc', '綠能環保業'),
                                                 ('36', 'otc', '數位雲端業'),
                                                 ('37', 'otc', '運動休閒業'),
                                                 ('38', 'otc', '居家生活業'),
                                                 ('80', 'otc', '管理股票'),
                                                 ('91', 'otc', '存託憑證')



