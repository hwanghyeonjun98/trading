package com.big15.tradingweb.dto;

import lombok.Data;

@Data
public class AccountHistoryDto {
	private String account_name;
	private String stock_code;
	private String buy_num;
	private String sell_num;
	private String his_time;
}
