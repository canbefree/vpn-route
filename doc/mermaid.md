```mermaid
    graph TD
        A(国内domain)
        B(ping,使用网关ping出国内ip地址)
        A-->B
```

通过dev代理流量 将国内流量通过dev iptable 环境访问?

- 代理是全局的，开发成本高 egge浏览器不使用代理，chrome使用代理？

