package com.big15.tradingweb.dto;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;

@Data
@Getter
@Setter
public class TradingDto {
	private String stock_code;
	private String stock_name;
	private String quantity;
	private String average_price;
	private String appraisal_amount;
	private String returns;
	private String book_value;
}
