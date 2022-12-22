package com.big15.tradingweb.dto;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;

@Data
@Getter
@Setter
public class AiTradingDto {
	private String code;
	private String name;
	private String amount;
	private String buyprice;
	private String evalValue;
	private String ratio;
	private String currentValue;
}
