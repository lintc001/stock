CREATE DATABASE IF NOT EXISTS stock;

USE stock;

/*
市場類別
*/
CREATE TABLE IF NOT EXISTS market (
	id VARCHAR(10) NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*
產業類別
*/
CREATE TABLE IF NOT EXISTS industry (
	id VARCHAR(10) NOT NULL,
	market_id VARCHAR(10) NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS company (
	id INT NOT NULL AUTO_INCREMENT,
	stock_code VARCHAR(20) NOT NULL,/*股票代碼*/
	stock_channel VARCHAR(100) NOT NULL,/*代碼加上國碼*/
	company_name VARCHAR(256) NOT NULL,
	short_name VARCHAR(256) NOT NULL,/*簡稱*/
	market_id VARCHAR(10) NOT NULL,
	industry_id VARCHAR(10) NOT NULL,
	
	founding_date DATE  NULL,/*成立日期*/
	ipo_date DATE  NULL,/*上市日期*/
	
	source_time DATETIME NOT NULL,/*資料日期*/
	update_time DATETIME NOT NULL,/*更新時間*/
	update_user VARCHAR(5) NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS second_price_2024_2330 (
	id INT NOT NULL AUTO_INCREMENT,
	stock_channel VARCHAR(100) NOT NULL,
	
	source_time DATETIME NOT NULL,
	latest_trade_price DECIMAL(6,4) NOT NULL,
	trade_volume INT NOT NULL,
	accumulate_trade_volume INT NOT NULL,
	
	update_time DATETIME NOT NULL,
	update_user VARCHAR(5) NOT NULL,
	
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS day_price_2024 (
	id INT NOT NULL AUTO_INCREMENT,
	stock_channel VARCHAR(100) NOT NULL,
	
	source_time DATETIME NOT NULL,
	`open` DECIMAL(6,4) NOT NULL,
	high DECIMAL(6,4) NOT NULL,
	low DECIMAL(6,4) NOT NULL,
	
	update_time DATETIME NOT NULL,
	update_user VARCHAR(5) NOT NULL,
	
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS observe_group(
	id INT NOT NULL AUTO_INCREMENT,
	stock_channel VARCHAR(100) NOT NULL,
	
	update_time DATETIME NOT NULL,
	update_user VARCHAR(5) NOT NULL,
	
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE IF NOT EXISTS observe_condition(
	id INT NOT NULL AUTO_INCREMENT,
	condi_type int NOT NULL,/*條件類型*/
	condi_name VARCHAR(255) NOT NULL,/*條件名稱*/
	remark VARCHAR(255) NOT NULL,
	observe_group_id INT NOT NULL,/*觀察的群組id*/
	
	update_time DATETIME NOT NULL,
	update_user VARCHAR(5) NOT NULL,
	
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;