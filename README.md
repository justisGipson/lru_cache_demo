### lru_cache decorator demo

lru = `Least Recently Used`

It works best when the most recent calls are the best predictors of upcoming calls.

`lru_cache` takes a parameter called `maxsize` - this limits the cache size. If `maxsize` is set
to `None`, the cache will have no limit. LRU performs best when the `maxsize` is a power of two(2)

This can almost be used anywhere, exception is functions with side-effect, functions that need to create
distinct mutable objects, or impure functions such as `time()` or `random()`

demoed with a simple Fibonacci Rescurion function - see [fib_nocache.py](fib_nocache.py) for an example.

Example output:

fibonacci with no `lru_cache`:
```
3
6
7
11
12
13
17
20
21
22
23
27
30
31
35
36
37
38
39
43
46
47
51
52
53
57
60
61
62
63
64
65
69
72
73
77
78
79
83
86
87
88
89
93
96
97
101
102
103
104
105
106
107
111
114
115
119
120
121
125
128
129
130
131
135
138
139
143
144
145
146
147
151
154
155
159
160
161
165
168
169
170
171
172
173
174
175
179
182
183
187
188
189
193
196
197
198
199
203
206
207
211
212
213
214
215
219
222
223
227
228
229
233
236
237
238
239
240
241
245
248
249
253
254
255
259
262
263
264
265
269
272
273
```

And with `lru_cache`:

```
3
4
5
6
7
8
9
10
```
