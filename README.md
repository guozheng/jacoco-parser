# jacoco-parser
A quick script to parse jacoco html report to generate code coverage numbers. Shamelessly borrowed the idea from [tavvasubbareddy's JacocoUtils in Java](https://github.com/tavvasubbareddy/JacocoUtils).

# Jacoco Coverage Report
`index.html` is a test coverage report file from [Jacoco's own coverage report](https://www.jacoco.org/jacoco/trunk/coverage/). It is a single line html file that contains coverage summary. The summary data looks like this (pretty printed):
```html
...
<thead>
        <tr>
          <td class="sortable" id="a" onclick="toggleSort(this)">Element</td>
          <td class="down sortable bar" id="b" onclick="toggleSort(this)">Missed Instructions</td>
          <td class="sortable ctr2" id="c" onclick="toggleSort(this)">Cov.</td>
          <td class="sortable bar" id="d" onclick="toggleSort(this)">Missed Branches</td>
          <td class="sortable ctr2" id="e" onclick="toggleSort(this)">Cov.</td>
          <td class="sortable ctr1" id="f" onclick="toggleSort(this)">Missed</td>
          <td class="sortable ctr2" id="g" onclick="toggleSort(this)">Cxty</td>
          <td class="sortable ctr1" id="h" onclick="toggleSort(this)">Missed</td>
          <td class="sortable ctr2" id="i" onclick="toggleSort(this)">Lines</td>
          <td class="sortable ctr1" id="j" onclick="toggleSort(this)">Missed</td>
          <td class="sortable ctr2" id="k" onclick="toggleSort(this)">Methods</td>
          <td class="sortable ctr1" id="l" onclick="toggleSort(this)">Missed</td>
          <td class="sortable ctr2" id="m" onclick="toggleSort(this)">Classes</td>
        </tr>
      </thead>
      <tfoot>
        <tr>
          <td>Total</td>
          <td class="bar">1,323 of 26,881</td>
          <td class="ctr2">95%</td>
          <td class="bar">141 of 2,074</td>
          <td class="ctr2">93%</td>
          <td class="ctr1">209</td>
          <td class="ctr2">2,558</td>
          <td class="ctr1">328</td>
          <td class="ctr2">6,228</td>
          <td class="ctr1">77</td>
          <td class="ctr2">1,489</td>
          <td class="ctr1">15</td>
          <td class="ctr2">289</td>
        </tr>
      </tfoot>
...
```
The script then uses regex to find those `<td>` element values and return a dictionary structure using counter name as key and a tuple `(missed, total, coverage_pct)` as value.

# Usage

```shell script
> python jacoco_parser.parser.py index.html
counter: METHODS - missed: 77, total: 1,489, coverage: 94.8287441236%
counter: CXTY - missed: 209, total: 2,558, coverage: 91.8295543393%
counter: INSTRUCTION - missed: 1,323, total: 26,881, coverage: 95.0783080987%
counter: LINES - missed: 328, total: 6,228, coverage: 94.7334617855%
counter: CLASSES - missed: 15, total: 289, coverage: 94.8096885813%
counter: BRANCH - missed: 141, total: 2,074, coverage: 93.2015429122%
```

`get_stats` returns the coverage data summary in the dictionary:
```python
{'METHODS': ('77', '1,489', 94.82874412357287), 'CXTY': ('209', '2,558', 91.8295543393276), 'INSTRUCTION': ('1,323', '26,881', 95.07830809865705), 'LINES': ('328', '6,228', 94.7334617854849), 'CLASSES': ('15', '289', 94.80968858131487), 'BRANCH': ('141', '2,074', 93.20154291224686)}
```