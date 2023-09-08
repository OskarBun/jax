# Copyright 2023 The JAX Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import os
from pathlib import Path
import platform
import sys

import jax._src.xla_bridge as xb

logger = logging.getLogger(__name__)


def initialize():
  path = Path(__file__).resolve().parent / "xla_cuda_plugin.so"
  if not path.exists():
    logger.warning(
        "WARNING: Native library %s does not exist. This most likely indicates"
        " an issue with how %s was built or installed.",
        path,
        __package__,
    )

  allocator = os.getenv("XLA_PYTHON_CLIENT_ALLOCATOR", "").lower()
  memory_fraction = os.getenv("XLA_PYTHON_CLIENT_MEMORY_FRACTION", "")
  preallocate = os.getenv("XLA_PYTHON_CLIENT_PREALLOCATE", "")

  options = {}
  if allocator not in ("default", "platform", "bfc", "cuda_async"):
    # defaults to bfc allocator
    allocator = "bfc"
  options["allocator"] = allocator
  if memory_fraction:
    options["memory_fraction"] = float(memory_fraction)
  if preallocate:
    options["preallocate"] = preallocate not in ("false", "False", "0")
  xb.register_plugin(
      "cuda", priority=500, library_path=str(path), options=options
  )
