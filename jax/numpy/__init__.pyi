import numpy as _np
from jax.numpy import fft, linalg
from typing import Any, Callable, Dict, Tuple, Type, Union
from jax._src.lax.lax import PrecisionLike
from jax._src.typing import Array, ArrayLike
from jax._src.numpy.index_tricks import _Mgrid, _Ogrid, CClass as _CClass, RClass as _RClass
from jax._src.numpy.reductions import CumulativeReduction as _CumulativeReduction
from jax._src.numpy.ufunc_api import ufunc as ufunc

class _UnaryUfunc:
  def __call__(self, x: ArrayLike, /) -> Array: ...

class _BinaryUfunc:
  def __call__(self, x1: ArrayLike, x2: ArrayLike, /) -> Array: ...

ComplexWarning: Any
abs: _UnaryUfunc
absolute: _UnaryUfunc
add: _BinaryUfunc
all: Any
allclose: Any
amax: Any
amin: Any
angle: Any
any: Any
append: Any
apply_along_axis: Any
apply_over_axes: Any
arange: Any
arccos: _UnaryUfunc
arccosh: _UnaryUfunc
arcsin: _UnaryUfunc
arcsinh: _UnaryUfunc
arctan: _UnaryUfunc
arctan2: _BinaryUfunc
arctanh: _UnaryUfunc
argmax: Any
argmin: Any
argpartition: Any
argsort: Any
argwhere: Any
around: Any
array: Any
array_equal: Any
array_equiv: Any
array_repr: Any
array_split: Any
array_str: Any
asarray: Any
atleast_1d: Any
atleast_2d: Any
atleast_3d: Any
average: Any
bartlett: Any
bfloat16: Any
bincount: Any
bitwise_and: _BinaryUfunc
bitwise_not: _UnaryUfunc
bitwise_or: _BinaryUfunc
bitwise_xor: _BinaryUfunc
blackman: Any
block: Any
bool_: Any
broadcast_arrays: Any
broadcast_shapes: Any
broadcast_to: Any
c_: _CClass
can_cast: Any
cbrt: _UnaryUfunc
cdouble: Any
ceil: _UnaryUfunc
character: Any
choose: Any
clip: Any
column_stack: Any
complex128: Any
complex64: Any
complex_: Any
complexfloating: Any
compress: Any
concatenate: Any
conj: _UnaryUfunc
conjugate: _UnaryUfunc
convolve: Any
copy: Any
copysign: _BinaryUfunc
corrcoef: Any
correlate: Any
cos: _UnaryUfunc
cosh: _UnaryUfunc
count_nonzero: Any
cov: Any
cross: Any
csingle: Any
cumprod: _CumulativeReduction
cumsum: _CumulativeReduction
deg2rad: _UnaryUfunc
degrees: _UnaryUfunc
delete: Any
diag: Any
diag_indices: Any
diag_indices_from: Any
diagflat: Any
diagonal: Any
diff: Any
digitize: Any
divide: _BinaryUfunc
def divmod(x: ArrayLike, y: ArrayLike, /) -> tuple[Array, Array]: ...
dot: Any
double: Any
dsplit: Any
dstack: Any
dtype: Any
e: Any
ediff1d: Any
einsum: Any
einsum_path: Any
empty: Any
empty_like: Any
equal: _BinaryUfunc
euler_gamma: Any
exp: _UnaryUfunc
exp2: _UnaryUfunc
expand_dims: Any
expm1: _UnaryUfunc
extract: Any
eye: Any
fabs: _UnaryUfunc
finfo: Any
fix: Any
flatnonzero: Any
flexible: Any
flip: Any
fliplr: Any
flipud: Any
float16: Any
float32: Any
float64: Any
float8_e4m3b11fnuz: Any
float8_e4m3fn: Any
float8_e4m3fnuz: Any
float8_e5m2: Any
float8_e5m2fnuz: Any
float_: Any
float_power: _BinaryUfunc
floating: Any
floor: _UnaryUfunc
floor_divide: _BinaryUfunc
fmax: _BinaryUfunc
fmin: _BinaryUfunc
fmod: _BinaryUfunc
def frexp(x: ArrayLike, /) -> tuple[Array, Array]: ...
from_dlpack: Any
frombuffer: Any
fromfile: Any
fromfunction: Any
fromiter: Any
def frompyfunc(func, /, nin, nout, *, identity = ...) -> ufunc: ...
fromstring: Any
full: Any
full_like: Any
gcd: _BinaryUfunc
generic: Any
geomspace: Any
get_printoptions: Any
gradient: Any
greater: _BinaryUfunc
greater_equal: _BinaryUfunc
hamming: Any
hanning: Any
heaviside: _BinaryUfunc
histogram: Any
histogram2d: Any
histogram_bin_edges: Any
histogramdd: Any
hsplit: Any
hstack: Any
hypot: _BinaryUfunc
i0: Any
identity: Any
iinfo: Any
imag: Any
in1d: Any
index_exp: Any
indices: Any
inexact: Any
inf: Any
inner: Any
insert: Any
int16: Any
int32: Any
int4: Any
int64: Any
int8: Any
int_: Any
integer: Any
interp: Any
intersect1d: Any
invert: _UnaryUfunc
isclose: Any
iscomplex: Any
iscomplexobj: Any
isfinite: _UnaryUfunc
isin: Any
isinf: _UnaryUfunc
isnan: _UnaryUfunc
isneginf: _UnaryUfunc
isposinf: _UnaryUfunc
isreal: Any
isrealobj: Any
isscalar: Any
issubdtype: Any
issubsctype: Any
iterable: Any
ix_: Any
kaiser: Any
kron: Any
lcm: _BinaryUfunc
ldexp: _BinaryUfunc
left_shift: _BinaryUfunc
less: _BinaryUfunc
less_equal: _BinaryUfunc
lexsort: Any
linspace: Any
load: Any
log: _UnaryUfunc
log10: _UnaryUfunc
log1p: _UnaryUfunc
log2: _UnaryUfunc
logaddexp: _BinaryUfunc
logaddexp2: _BinaryUfunc
logical_and: _BinaryUfunc
logical_not: _UnaryUfunc
logical_or: _BinaryUfunc
logical_xor: _BinaryUfunc
logspace: Any
mask_indices: Any
def matmul(
    a: ArrayLike, b: ArrayLike, *, precision: PrecisionLike = None
) -> Array: ...
matrix_transpose: Any
max: Any
maximum: _BinaryUfunc
mean: Any
median: Any
meshgrid: Any
mgrid: _Mgrid
min: Any
minimum: _BinaryUfunc
mod: _BinaryUfunc
def modf(x: ArrayLike, /, out=None) -> tuple[Array, Array]: ...
moveaxis: Any
multiply: _BinaryUfunc
nan: Any
nan_to_num: Any
nanargmax: Any
nanargmin: Any
nancumprod: _CumulativeReduction
nancumsum: _CumulativeReduction
nanmax: Any
nanmean: Any
nanmedian: Any
nanmin: Any
nanpercentile: Any
nanprod: Any
nanquantile: Any
nanstd: Any
nansum: Any
nanvar: Any
ndarray = Array
ndim: Any
negative: _UnaryUfunc
newaxis: Any
nextafter: _BinaryUfunc
nonzero: Any
not_equal: _BinaryUfunc
number: Any
object_: Any
ogrid: _Ogrid
ones: Any
ones_like: Any
outer: Any
packbits: Any
pad: Any
partition: Any
percentile: Any
pi: Any
piecewise: Any
place: Any
poly: Any
polyadd: Any
polyder: Any
polydiv: Any
polyfit: Any
polyint: Any
polymul: Any
polysub: Any
polyval: Any
positive: _UnaryUfunc
power: _BinaryUfunc
printoptions: Any
prod: Any
product: Any
promote_types: Any
ptp: Any
put: Any
quantile: Any
r_: _RClass
rad2deg: _UnaryUfunc
radians: _UnaryUfunc
ravel: Any
ravel_multi_index: Any
real: Any
reciprocal: _UnaryUfunc
register_jax_array_methods: Any
remainder: _BinaryUfunc
repeat: Any
reshape: Any
resize: Any
result_type: Any
right_shift: _BinaryUfunc
rint: _UnaryUfunc
roll: Any
rollaxis: Any
roots: Any
rot90: Any
round: Any
round_: Any
row_stack: Any  # TODO(jakevdp): remove this
s_: Any
save: Any
savez: Any
searchsorted: Any
select: Any
set_printoptions: Any
setdiff1d: Any
setxor1d: Any
shape: Any
sign: _UnaryUfunc
signbit: _UnaryUfunc
signedinteger: Any
sin: _UnaryUfunc
sinc: Any
single: Any
sinh: _UnaryUfunc
size: Any
sort: Any
sort_complex: Any
split: Any
sqrt: _UnaryUfunc
square: _UnaryUfunc
squeeze: Any
stack: Any
std: Any
subtract: _BinaryUfunc
sum: Any
swapaxes: Any
take: Any
take_along_axis: Any
tan: _UnaryUfunc
tanh: _UnaryUfunc
tensordot: Any
tile: Any
trace: Any
transpose: Any
trapz: Any
tri: Any
tril: Any
tril_indices: Any
tril_indices_from: Any
trim_zeros: Any
triu: Any
triu_indices: Any
triu_indices_from: Any
true_divide: _BinaryUfunc
trunc: _UnaryUfunc
typing: Any
uint: Any
uint16: Any
uint32: Any
uint4: Any
uint64: Any
uint8: Any
union1d: Any
unique: Any
unpackbits: Any
unravel_index: Any
unsignedinteger: Any
unwrap: Any
vander: Any
var: Any
vdot: Any
def vectorize(pyfunc, *, excluded = ..., signature = ...) -> Callable: ...
vsplit: Any
vstack: Any
where: Any
zeros: Any
zeros_like: Any
