# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class NvplScalapack(Package):
    """
    NVPL ScaLAPACK (NVIDIA Performance Libraries ScaLAPACK) provides an optimized implementation
    of ScaLAPACK for distributed-memory architectures.

    The software supports a wide range of distributed parallel dense linear algebra operations,
    solving dense and banded linear systesms, least-square problems, eigenvalue and singular
    value problems.
    """

    homepage = "https://docs.nvidia.com/nvpl/_static/scalapack/index.html"
    url = ("https://developer.download.nvidia.com/compute/nvpl/redist"
           "/nvpl_scalapack/linux-sbsa/nvpl_scalapack-linux-sbsa-0.1.0.1-archive.tar.xz")

    maintainers("albestro")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list.
    license("UNKNOWN")

    version("0.1.0", sha256="5529901e214bd3eb9e7d9ad73d196b3c8950b81943b776c4d8013b4a7f430268")

    provides("scalapack")

    # TODO add compiler requirements

    def install(self, spec, prefix):
        install_tree(".", prefix)
