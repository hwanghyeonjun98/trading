package com.big15.tradingweb.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class DeveloperController {
	@GetMapping("/developer/developer_info")
	public String infoPage() {
		return "/developer/developer_info";
	}
}
