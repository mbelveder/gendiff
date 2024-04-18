[![Actions Status](https://github.com/mbelveder/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/mbelveder/python-project-50/actions) [![Maintainability](https://api.codeclimate.com/v1/badges/c2f7440684c2dd83210a/maintainability)](https://codeclimate.com/github/mbelveder/python-project-50/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/c2f7440684c2dd83210a/test_coverage)](https://codeclimate.com/github/mbelveder/python-project-50/test_coverage)

### Description

A Python package to generate a diff between two nested structures.

![Example](docs/media/example.png)

Works both with JSON and YAML files and supports pretty-printed (default), plain and json-string output format:

[![asciicast](https://asciinema.org/a/HuOgkKzA76RJu0G6MsUYq7OMM.svg)](https://asciinema.org/a/HuOgkKzA76RJu0G6MsUYq7OMM)

Created during the [Hexlet](https://ru.hexlet.io/programs/python) "Python developer" course.

### Requirements

- Python 3.11 or higher
- Git


### Installation

```
git install git+https://github.com/mbelveder/gendiff.git
```

<!-- <details>
<summary>Example (open on a wide screen)</summary>
<table>
<tr>
<td > file1.json </td>
<td > file2.json </td>
<td > diff </td>
</tr>
<tr>
<td style="vertical-align:top">

```json
{
    "common": {
      "node1": "val 1",
      "node2": 200,
      "node3": true,
      "node6": {
        "key": "val",
        "doge": {
          "wow": ""
        }
      }
    },
    "group1": {
      "baz": "bas",
      "foo": "bar",
      "nest": {
        "key": "val"
      }
    },
    "group2": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  }
```
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

</td>
<td style="vertical-align:top">
    
```json
{
  "common": {
    "follow": false,
    "node1": "val 1",
    "node3": null,
    "node4": "blah",
    "node5": {
      "key5": "val5"
    },
    "node6": {
      "key": "val",
      "ops": "vops",
      "doge": {
        "wow": "cool"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 101
  }
}
```
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>

</td>
</td>
<td style="vertical-align:top">
    
```text
{
  common: {
  + follow: false
    node1: val 1
  - node2: 200
  - node3: true
  + node3: null
  + node4: blah
  + node5: {
      key5: val5
    }
    node6: {
      doge: {
      - wow: 
      + wow: cool
      }
      key: val
    + ops: vops
    }
  }
  group1: {
  - baz: bas
  + baz: bars
    foo: bar
  - nest: {
      key: val
    }
  + nest: str
  }
- group2: {
    abc: 12345
    deep: {
      id: 45
    }
  }
+ group3: {
    deep: {
      id: {
        number: 45
      }
    }
    fee: 101
  }
}
```
</td>
</tr>
</table>

</details> -->


### Topics covered:

- Test-driven development

- Recursive tree traversal

- Separation of abstraction layers (the [diff itself](https://github.com/mbelveder/gendiff/blob/e2e005ddab480fcbc5a80a70fa71f466e8c0e808/gendiff/generate_diff.py#L16) is separate from its representations)

- Continuous integration via GitHub Actions

- Dependency management via [Poetry](https://python-poetry.org/)