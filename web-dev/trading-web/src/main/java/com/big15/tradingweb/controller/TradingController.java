package com.big15.tradingweb.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpServletRequest;
import java.util.Locale;

@Controller
@RequestMapping("/")
public class TradingController {
	@GetMapping("/")
	public String browserCheck(HttpServletRequest request, Locale locale, Model model) {
		String browser= "";
		String userAgent = request.getHeader("User-Agent");

		if(userAgent.indexOf("Trident") > -1) {
			return "/errors/browser_info";
		}

		return "index";
	}
}
