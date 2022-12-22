package com.big15.tradingweb.dto;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;

@Data
@Getter
@Setter
public class MarketCapDto {
	private String no;
	private String stock_name;
	private String market_cap;
}
