package com.big15.tradingweb.config;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.SqlSessionTemplate;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.jdbc.DataSourceBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;

import javax.sql.DataSource;

@Configuration
@MapperScan(value = "com.big15.tradingweb.mapper", sqlSessionFactoryRef = "factory")
public class WebDataConfig {
	@Primary
	@Bean(name = "webdata")
	@ConfigurationProperties(prefix = "spring.datasource.webdata")
	public DataSource doSource() {
		return DataSourceBuilder.create().build();
	}

	@Primary
	@Bean(name = "factory")
	public SqlSessionFactory sqlSesstionFactory(DataSource dataSource) throws Exception {
		SqlSessionFactoryBean sqlSessionFactory = new SqlSessionFactoryBean();
		sqlSessionFactory.setDataSource(dataSource);
		sqlSessionFactory.setTypeAliasesPackage("com.big15.tradingweb.mapper");
		sqlSessionFactory.setMapperLocations(new PathMatchingResourcePatternResolver().getResources("classpath:/mybatis/mapper/webData/*.xml"));
		return sqlSessionFactory.getObject();
	}

	@Primary
	@Bean(name = "sqlSession")
	public SqlSessionTemplate sqlSession(SqlSessionFactory sqlSessionFactory) {
		return new SqlSessionTemplate(sqlSessionFactory);
	}
}
