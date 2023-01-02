package com.big15.tradingweb.dto;

import lombok.Data;

@Data
public class AccountHistoryDto {
	private String account_name;
	private String his_time;
	private String code_name;
	private String date;
	private String stock_code;
	private String buy_num;
	private String sell_num;
	private String amount;
	private String ratio;
	private String profit;
}
