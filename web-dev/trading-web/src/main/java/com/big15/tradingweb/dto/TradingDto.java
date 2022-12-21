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
	private int quantity;
	private double average_price;
	private int appraisal_amount;
	private double returns;
	private double book_value;
}
