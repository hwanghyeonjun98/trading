package com.big15.tradingweb.controller;

import com.big15.tradingweb.model.Project;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Date;

@RestController
public class TradingRestController {
	@GetMapping("/api/test")
	public Object dataView() {
		Project project = new Project();
		project.projectName = "preword";
		project.author = "hello-bryan";
		project.createdDate = new Date();
		return project;
	}
}
