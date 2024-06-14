---
marp: true
paginate: true
class: invert
style: |
  h1 {
    color: #F2A30F;
    text-align: center;
  }
---

# package management with `pixi`

<br>


<div align="center">

![height:300](https://github.com/jjjermiah/pixi-vscode/blob/main/assets/images/VSCode-Pixi-Logo.png?raw=true)

[![height:50](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/prefix-dev/pixi/main/assets/badge/v0.json)](https://pixi.sh)

</div>

---

# What is `pixi`?

> `pixi` is a fast software package manager built on top of the existing conda ecosystem. Spins up development environments quickly on Windows, macOS and Linux.

---

# Another package manager 🧐?

| Tool     | Installs Python | Builds Packages | Task Runner | Built-in lockfiles | Fast | Python-Independent | Install Conda Pkgs |
| -------- | --------------- | --------------- | ----------- | ------------------ | ---- | ------------------ | ------------------ |
| `conda`  | ✅              | ❌              | ❌          | ❌                 | ❌   | ❌                 | ✅                 |
| `mamba`  | ✅              | ❌              | ❌          | ❌                 | ✅   | ✅                 | ✅                 |
| `pip`    | ❌              | ✅              | ❌          | ❌                 | ❌   | ❌                 | ❌                 |
| `uv`     | ❌              | ❌              | ❌          | ❌                 | ✅   | ✅                 | ❌                 |
| `poetry` | ❌              | ✅              | ❌          | ✅                 | ❌   | ❌                 | ❌                 |
| `pixi`   | ✅              | ✅              | ✅          | ✅                 | ✅   | ✅                 | ✅                 |

---

# Easy Installation & Update

```console
# Linux & macOS
$ curl -fsSL https://pixi.sh/install.sh | bash

# Windows
$ iwr -useb https://pixi.sh/install.ps1 | iex
```

```console
# Update
$ pixi self-update
```

---

# `pixi` is fast 🚀

![bench](./benchmarks/results/benchmarks.png)

---

# Global Tool Installation

Install conda pkgs globally, with each of them having their own environment.

- no more `base` conda envs!

```console

$ pixi global install hyperfine ripgrep fzf zoxide
✔ Installed package hyperfine 1.18.0 h5ef7bb8_0 from conda-forge
✔ Installed package ripgrep 14.1.0 h5ef7bb8_0 from conda-forge
✔ Installed package fzf 0.53.0 h75b854d_0 from conda-forge
✔ Installed package zoxide 0.9.4 h5ef7bb8_1 from conda-forge
  These executables are now globally available:
   -  hyperfine
   -  rg
   -  fzf
   -  zoxide

```

---

# Use both `conda` and `pip` packages together

`pixi` solves environments across multiple package managers.

```toml

[dependencies] # conda packages
python = ">3.9"

[pypi-dependencies] # pip packages
damply = "*"

```

---

# Other package managers

```toml

[dependencies]
yarn = ">=4.3.0,<4.4"

[tasks]
build = "yarn build-pdf"
serve = "yarn build-html"

```

---

# Project level features

Features are a way to group dependencies and tasks together.

- allow for logical grouping, and saves any headaches from dependency conflicts.

```toml

[features.docs]
dependencies = ["mkdocs", "mkdocs-material"]
tasks = { serve = "mkdocs serve" }

[features.r]
dependencies = ["r-base", "r-essentials", "bioconductor-pharmacogx"]
tasks = { pgx = "Rscript -e 'library(pharmacogx); pharmacogx::someFunction()'" }

```

---

# Lockfiles

`pixi` generates a lockfile `pixi.lock` that:

- is human-readable
- can be checked into version control like `git`
  - no more `environment.yml` files!
- can be used to recreate the exact environment on another machine
- solves multiple environments _across_ **multiple machine types**

---

# Sidestep activation

No `conda activate` or `conda deactivate` needed!

- per-directory envs are automatically found and commands are run in the correct env.

```console
$ pixi run --environment docs mkdocs --serve
```

<br>
if you truly wish to activate an env, you can do so with `pixi shell`.

```console
$ pixi shell --environment docs
$ (docs) mkdocs --serve
```

---

# Tasks

Run tasks in the correct environment, without needing to activate it.

```toml
# assume the following in your pyproject.toml
[tool.pixi.feature.docs.tasks]
serve = "mkdocs serve"
```

<br>

`pixi` will automatically activate the correct environment and run the task.

```console
$ pixi run serve
```

---

# these slides were generated using `pixi tasks` !

[![](https://mermaid.ink/img/pako:eNp9Uk1PwzAM_StWztsfyIHDNCEOICa2CyIcssZdI5o0ygeimvbfiZOpK4ORQ-06fvbzc46sGRQyzg5eug52a2Ehn5D2NbBC23RG-o9QL-jsKfYmWLEcXpINEDus8ZILKWh7gG506FttUbD3C9z1Q8xoMhw2-fsLfUCLXkZUsB9vFAlReqpSLIdnh2cSFyw1WIBMcTAy6kb2_QieuE6dQLdgERWqqTZadaXAq_R2NnvSvVp20fQkwPTDYUV-YfCwe3qE0GuF4Sdl9J9IlMly2JL5F1DLO9VOrbI_77RZ3_-Fwy83FHGqU9W5BSgDV5cEg-Xyrgp0loH0LUG6rbHL2FcXZbJaYUqZQzL9K0RlOIPkFGHZghn0RmqVH-aRMgXL9E1-Ajy7Kq9OMGFPOY_Wux1tw3j0CRcsOZWXv9YyL88w3so-4OkbpF7y3Q?type=png)](https://mermaid.live/edit#pako:eNp9Uk1PwzAM_StWztsfyIHDNCEOICa2CyIcssZdI5o0ygeimvbfiZOpK4ORQ-06fvbzc46sGRQyzg5eug52a2Ehn5D2NbBC23RG-o9QL-jsKfYmWLEcXpINEDus8ZILKWh7gG506FttUbD3C9z1Q8xoMhw2-fsLfUCLXkZUsB9vFAlReqpSLIdnh2cSFyw1WIBMcTAy6kb2_QieuE6dQLdgERWqqTZadaXAq_R2NnvSvVp20fQkwPTDYUV-YfCwe3qE0GuF4Sdl9J9IlMly2JL5F1DLO9VOrbI_77RZ3_-Fwy83FHGqU9W5BSgDV5cEg-Xyrgp0loH0LUG6rbHL2FcXZbJaYUqZQzL9K0RlOIPkFGHZghn0RmqVH-aRMgXL9E1-Ajy7Kq9OMGFPOY_Wux1tw3j0CRcsOZWXv9YyL88w3so-4OkbpF7y3Q)

<br>
Running `pixi run export` will run the benchmark, plot them, and import them before exporting these slides.

---

# multi-environments

Create multiple environments in a single project.

- this allows for different dependencies for different tasks.
- ensures that they are solved with the correct dependencies.

```toml

[environments]
dev = { features = ["docs", "tests"] }
test = { features = ["tests"] }
publish = { features = ["docs", "release"] }


```

---

# multi-environments (cont.)

Allows for testing across multiple python-versions across multiple environments.

```toml

[environments]
testpy39 = { features = ["py39", "tests"] }
testpy310 = { features = ["py310", "tests"] }
testpy311 = { features = ["py311", "tests"] }

```

---

# multi-platform

No more "it works on my machine"!

- `pixi` lockfiles are platform-independent
- solves every environment across multiple platforms
  - determine in real-time if a package is not available on a platform
    <br>

```toml

[project]
platforms = ["win-64", "linux-64", "osx-64", "osx-arm64"]

```

---

# Complex Dependency Resolution

all the configurations can be defined at the **_feature_** level.

```toml
[project]
channels = ["conda-forge"]
platforms = ["linux-64", "linux-aarch64","osx-64", "win-64"]

[feature.cuda]
channels = ["nvidia", "conda-forge"]
platforms = ["linux-64"] # only going to use this on linux

[feature.cuda.dependencies]
cudatoolkit = "*"
pytorch-cuda = { version = "12.1", channel = "pytorch" }

[feature.cuda.tasks]
train-model = "python train.py --cuda"
evaluate-model = "python evaluate.py --cuda"
# running `pixi run model` will run both tasks in the correct environment
model = { depends_on = ["train-model", "evaluate-model"]}
```

---

# TL;DR

# reproducible **EVERYTHING** with `pixi`

---
