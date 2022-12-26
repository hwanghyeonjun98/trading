package com.big15.tradingweb.controller;

import com.big15.tradingweb.dto.InvestingDto;
import com.big15.tradingweb.dto.NewsDto;
import com.big15.tradingweb.mapper.IndexdataMapper;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpServletRequest;
import java.util.List;
import java.util.Locale;

@Slf4j
@Controller
@AllArgsConstructor
@RequestMapping(value = {"/", "/index"})
public class TradingController {

	private IndexdataMapper indexdataMapper;

	// 브라우저 체크
	// index 페이지 접근시 브라우저가 인터넷 익스플로러면
	// 다른 브라우저 접속 다운로드 안내 페이지로 이동
	@GetMapping("")
	public String Index(HttpServletRequest request, Locale locale, Model model) {
		String userAgent = request.getHeader("User-Agent");

		if (userAgent.indexOf("Trident") > -1) {
			model.addAttribute("msg", "Internet Explorer는 호환되지 않는 브라우저 입니다.");
			return "/errors/browser_info";
		}
		
		List<InvestingDto> kospi_ = indexdataMapper.kospidata();
		model.addAttribute("kospidata",kospi_);

		List<NewsDto> news = indexdataMapper.newsdata();
		model.addAttribute("nnews", news);
		
		return "index";
	}
	
	

}
