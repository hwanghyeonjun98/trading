package com.big15.tradingweb.controller;

import com.big15.tradingweb.dto.UserInfoDto;
import com.big15.tradingweb.mapper.JoinMapper;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@Slf4j
@RestController
@AllArgsConstructor
@RequestMapping("/join")
public class JoinRestController {

	JoinMapper joinMapper;

	@PostMapping("/userJoin")
	public void join(@RequestParam(value = "user_id") String user_id
		, @RequestParam(value = "user_pw", required = false) String user_pw
		, @RequestParam(value = "user_name", required = false) String user_name
		, @RequestParam(value = "user_account", required = false) String user_account
		, HttpServletResponse response) throws IOException {
		int join = joinMapper.join(user_id, user_pw, user_name, user_account);

		if (join == 0) {
			response.getWriter().print("joinFalse");
		}

		if (join == 1) {
			response.getWriter().print("joinTrue");
		}
	}

	@RequestMapping("/idCheck/{user_id}")
	public void idCheck(@PathVariable("user_id") String user_id, HttpServletResponse response) throws IOException {
		List<UserInfoDto> user = joinMapper.idCheck(user_id);
		System.out.println(user);

		if (user.size() == 0) {
			response.getWriter().print("notId");
		}

		if (user.size() > 0) {
			response.getWriter().print("hadId");
		}
	}
}
