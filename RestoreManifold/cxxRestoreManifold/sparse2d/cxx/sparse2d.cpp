#include "starlet2d.h"

using namespace boost::python;

BOOST_PYTHON_MODULE(starlet2d)
{
	np::initialize();

	class_< Starlet2D >("Starlet2D", init<int, int, int,int,int >())
	  .def("forward2d", &Starlet2D::transform_numpy)
	  .def("forward2d_omp", &Starlet2D::transform_omp_numpy)
	  .def("forward1d_omp", &Starlet2D::transform1d_omp_numpy)
	  .def("backward2d", &Starlet2D::reconstruct_numpy)
	  .def("adjoint1d",&Starlet2D:: adjoint1d_omp_numpy)
	  .def("backward2d_omp", &Starlet2D::reconstruct_omp_numpy);
}
